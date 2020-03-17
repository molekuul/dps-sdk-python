import binascii
import json
import uuid
import copy
from collections import ChainMap

# The following lines are used even if the inspector shows otherwise
from dvlssdk.generated import models
from dvlssdk.custom import models
from dvlssdk.custom.SDKResult import SDKResult
from dvlssdk.generated import enums
from dvlssdk.InitHelpers import *
from dvlssdk.ApiManager import ApiManager, Encoder
from dvlssdk.DvlsLogger import DvlsLogger

from dvlssdk import URLConstants, CSV_FileOps, ConnectionValidation
from dvlssdk.EntryType import *
from dvlssdk.EncryptionUtils import EncryptionManager
from dvlssdk.generated.enums.PasswordGeneratorMode import PasswordGeneratorMode

from ._version import get_versions

class DVLSConnection:
    """
    Use this class and its methods to interact with a DVLS server

    :param dvlsURI: address of the server
    :param options: specify log='ERROR' or 'WARNING' to output the desired type of messages to the console,
                        or omit to display all messages (info, warning & errors)
    """

    GWCCID_UsePrvVltSrch = '88E4BE76-4C5B-4694-AA9C-D53B7E0FE0DC'
    GWCCID_UseCredRepoPrompt = '00000000-0000-0000-0000-000000000000'
    GWCCID_UsePersoCred = '9F3C3BCF-068A-4927-B996-CA52154CAE3B'
    DEFAULT_REPO_GUID = GWCCID_UseCredRepoPrompt

    STANDARD_ENTRY_TYPES = STANDARD_ENTRY_TYPES
    CONTACT_ENTRY_TYPES = CONTACT_ENTRY_TYPES
    DATA_ENTRY_TYPES = DATA_ENTRY_TYPES
    CREDENTIAL_ENTRY_TYPES = CREDENTIAL_ENTRY_TYPES

    AESSessionKey = None
    DvlsTokenID = None
    DvlsUserLoggedIn = None
    DvlsURI = None
    DvlsRequestHeaders = None

    __version__ = get_versions()['version']

    def __init__(self, dvlsuri, **options):
        verbose = True
        if 'verbose' in options:
            verbose = options.get('verbose')
        options['version'] = self.__version__
        self.dvls_logger = DvlsLogger(options)
        self.dvls_logger.set_verbose(verbose)
        self.version = get_versions()

        self._api = ApiManager(dvlsuri, self.dvls_logger)

    def login(self, username, password, verbose_override=None):
        """
        Logs in a user to the DVLS server

        :param username: username of the user to log in
        :param password: password of the user to log in
        :param verbose_override: default verbose_override=None to keep default verbose of ApiManager
        :return: SDKResult
        """
        result = SDKResult()
        if isinstance(username, str) and isinstance(password, str):
            result = self._api.login(username, password, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.login] - Successful for " + username, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.login] - Failed for" + username, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.login] - Username and password parameters must be strings", verbose_override)
        return result

    def logout(self, username, verbose_override=None):
        """
        Logs out a user from the DVLS server

        :param username: username of the user to log out
        :param verbose_override: default verbose_override=None to keep default verbose of ApiManager
        :return: SDKResult
        """
        result = self._api.logout(username, verbose_override)
        if result.success:
            self.dvls_logger.info("[DvlsSDK.logout] - Successful for " + username, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.logout] - Failed for" + username, verbose_override)
        return result

    def get_server_info(self, verbose_override = None):
        """
        Get server information

        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': ServerInformation (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_server_info()
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_server_info] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_server_info] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_server_info] - No user logged in, aborting getting server info",
                                   verbose_override)
        return result

    def create_user(self, user_type, username, password, **options):
        """
        Creates a DVLS server user

        - A database('SqlServer') user does not need a password specified only if it already exists in the database.
        - A database('SqlServer') user needs a password specified if the auto-create database user option is activated
                                                and the user does not already exist in the database.
        - A domain('Domain') user does not need a password; specify None

        :param user_type: type of the user to create ('SqlServer', 'Builtin' or 'Domain')
        :param username: username of the user to create
        :param password: password of the user to create
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        - IsAdministrator - user is an Admin or not - True or False
        - IsEnabled - user is active or not - True or False
        - UserMustChangePasswordAtNextLogon - force user to change his password next time he logs in - True or False
        - Email - email address of the user
        - FirstName - first name of the user
        - LastName - last name of the user
        - CompanyName - company name of the user
        - JobTitle - job title of the user
        - Department - department of the user
        - GravatarEmail - gravatar email of the user
        - Address - address of the user
        - State - state name where the user lives
        - CountryCode - country code of the country where the user lives (ex: 'CA', 'US', 'DE')
        - Phone - phone number of the user
        - Workphone - work phone number of the user
        - CellPhone - cell phone number of the user
        - Fax - fax phone number of the user
        - HasAccessPVM - user has access to PVM or not - True or False
        - HasAccessRDM - user has access to RDM or not - True or False
        - HasAccessWeb - user has access to the dvls server web site or not - True or False
        - HasAccessWebLogin - user has access to WebLogin or not - True or False
        - CustomRoles - list of roles that the user can be affected - depends on the
            current roles added to the DVLS server
        - AllowDragAndDrop - user is allowed to drag and drop or not - True or False
        - AllowRevealPassword - user is allowed to reveal password or not - True or False
        - CanExport - user is allowed to export or not - True or False
        - CanImport - user is allowed to import or not - True or False
        - CanViewDetails - user is allowed to view details or not - True or False
        - CanViewGlobalLogs - user is allowed to view usage logs or not - True or False
        - CanViewInformations - user is allowed to view informations or not - True or False
        - OfflineMode - user is allowed which offline permissions - 'Disabled', 'ReadOnly' or 'ReadWrite'
        :return: SDKResult{'data': UserEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            result = self.get_user_by_name(username, verbose_override)
            if result.success:
                self.dvls_logger.error("[DvlsSDK.create_user] - User '" + username +
                                       "' already exists", verbose_override)
            else:
                options['Name'] = username
                if password:
                    if user_type == 'SqlServer' or user_type == 'Builtin':
                        options['Password'] = bytes.decode(binascii.hexlify(self._api.EncryptionManager.aes_encrypt(password)))
                    if user_type == 'Domain':
                        self.dvls_logger.warning("[DvlsSDK.create_user] - Ignoring password data. Domain users " +
                                                 "do not need to set a password", verbose_override)
                else:
                    if user_type == 'Builtin':
                        self.dvls_logger.error("[DvlsSDK.create_user] - Password required to create Custom users, " +
                                               "aborting creation of user " + username, verbose_override)
                        return SDKResult(result)
                new_user = init_model('generated', 'UserEntity')
                new_user.UserSecurity.CustomSecurityEntity = init_model('generated', 'CustomSecurity')
                new_user.UserAccount.TwoFactorInfo = init_model('generated', 'TwoFactorInfo')
                new_user = fill_data(new_user, options)
                server_user_type = init_enum('generated', 'ServerUserType')
                new_user.UserSecurity.AuthenticationType = server_user_type.value_from_name(user_type)

                result = self._api.save_user(new_user, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.create_user] - Successful for " + username, verbose_override)
                    if isinstance(result.data, dict) and 'key' in result.data:
                        result.data['id'] = result.data['key']
                else:
                    self.dvls_logger.error("[DvlsSDK.create_user] - Failed for " + username, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_user] - No user logged in, aborting creation of user " +
                                   username, verbose_override)
        return result

    def get_user_by_name(self, username, verbose_override=None):
        """
        Retrieve a user entry using it's unique name

        :param username: Name of the user that needs its info retrieved
        :param verbose_override: overrides the logger verbose level
        :return: SDKResult{'data': UserEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            users_result = self._api.get_users(verbose_override)
            if users_result.success:
                users = users_result.data
                for user in users:
                    if user['display'] == username:
                        user['id'] = user['key']
                        result.data = user
                        break
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_user_by_name] - Successful for " + username, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_user_by_name] - Failed for " + username, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_user_by_name] - No user logged in, aborting get user " + username,
                                   verbose_override)
        if result.success:
            self.dvls_logger.info("[DvlsSDK.get_user_by_name] - Successful for " +
                                  username, verbose_override)
        return result

    def get_user_by_id(self, user_id, verbose_override=None):
        """
        Retrieve the user with given id

        :param user_id: ID of the user wanted
        :param verbose_override: overrides the logger verbose level
        :return: SDKResult{'data': UserEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_user(user_id, verbose_override)
            if result.success:
                if isinstance(result.data, dict) and 'key' in result.data:
                    result.data['id'] = result.data['key']
                self.dvls_logger.info("[DvlsSDK.get_user_by_id] - Successful for " + str(user_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_user_by_id] - Failed for " + str(user_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_user_by_id] - No user logged in, aborting get user " + str(user_id), verbose_override)
        if result.data == {}:
            result.data = None
        return result

    def get_user_id(self, username, verbose_override=None):
        """
        Retrieve a user's unique id

        :param username: name of the user that needs its id retrieved
        :param verbose_override: overrides the logger verbose level
        :return: SDKResult{'data': Guid (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self.get_user_by_name(username, verbose_override)
            if result.success:
                user_info = result.data
                if 'key' in user_info:
                    result.data = user_info['key']
                    self.dvls_logger.info("[DvlsSDK.get_user_id] - Successful for " + username, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.get_user_id] - Failed for " + username, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_user_id] - Error getting user info, aborting get id of user " +
                                       username, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_user_id] - No user logged in, aborting get id of user " +
                                   username, verbose_override)
        return result

    def get_users(self, verbose_override=None):
        """
        Retrieve list of all users

        :param verbose_override: overrides the logger verbose level
        :return: SDKResult{'data': tree of UserEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_users(verbose_override)
            if result.success:
                for u in result.data:
                    u['id'] = u['key']
                self.dvls_logger.info("[DvlsSDK.get_users] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_users] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_users] - No user logged in, aborting get_users", verbose_override)
        return result

    def modify_user_by_name(self, username, **options):
        """
        Modifies a user

        :param username: Name of the user to modify
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        - AuthenticationType - User authentication method values: 'Domain', 'SqlServer', 'Builtin'
        - Password: User password
        - CustomRoles: List of CustomRole names to apply to user

        :return: SDKResult{'data': UserEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            info_result = self.get_user_by_name(username, verbose_override)
            if not info_result.success:
                self.dvls_logger.error("[DvlsSDK.modify_user_by_name] - User '" + username + "' does not exist",
                                       verbose_override)
                return result
            else:
                user_info = info_result.data
                if 'Name' not in options:
                    options['Name'] = username
                new_user = self._generate_user_entity(user_info, options, verbose_override)
                if new_user is None:
                    self.dvls_logger.error("[DvlsSDK.modify_user_by_name] - Problem generating user to save, " +
                                           "aborting modification of user " + username, verbose_override)
                else:
                    result = self._api.modify_user(new_user, verbose_override)
                    if result.success:
                        if isinstance(result.data, dict) and 'key' in result.data:
                            result.data['id'] = result.data['key']
                        self.dvls_logger.info("[DvlsSDK.modify_user_by_name] - Successful for " + username,
                                              verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.modify_user_by_name] - Failed for " + username,
                                               verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_user_by_name] - No user logged in, aborting modification of user " +
                                   username, verbose_override)
        return result

    def modify_user_by_id(self, user_id, **options):
        """
        Modifies a user

        :param user_id: ID of the user to modify
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        - AuthenticationType - User authentication method values: 'Domain', 'SqlServer', 'Builtin'
        - Password: User password
        - CustomRoles: List of CustomRole names to apply to user

        :return: SDKResult{'data': UserEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            info_result = self.get_user_by_id(user_id, verbose_override)
            if not info_result.success:
                self.dvls_logger.error("[DvlsSDK.modify_user_by_id] - User '" + str(user_id) +
                                       "' does not exist", verbose_override)
                return result
            else:
                user_info = info_result.data
                new_user = self._generate_user_entity(user_info, options, verbose_override)
                if new_user is None:
                    self.dvls_logger.error("[DvlsSDK.modify_user_by_id] - Problem generating user to save, " +
                                           "aborting modification of user " + str(user_id), verbose_override)
                else:
                    result = self._api.modify_user(new_user, verbose_override)
                    if result.success:
                        if isinstance(result.data, dict) and 'key' in result.data:
                            result.data['id'] = result.data['key']
                        self.dvls_logger.info("[DvlsSDK.modify_user_by_id] - Successful for " + str(user_id),
                                              verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.modify_user_by_id] - Failed for " + str(user_id),
                                               verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_user_by_id] - No user logged in, aborting modification of user " +
                                   str(user_id), verbose_override)
        return result

    def delete_user_by_name(self, username, verbose_override=None):
        """
        Deletes a user

        :param username: Name of the user to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            info_result = self.get_user_by_name(username, verbose_override)
            if not info_result.success:
                self.dvls_logger.error("[DvlsSDK.delete_user_by_name] - Cannot delete user '" + username +
                                       "' could not get userinfo", verbose_override)
                return result
            user_info = info_result.data
            if user_info['userSecurity']['serverUserTypeString'] == "Database":
                self.dvls_logger.warning("[DvlsSDK.delete_user_by_name] - DB user '" + username +
                                         "' deleted in DVLS, not in the SQL DB", verbose_override)
            user_key = None
            if 'key' in user_info:
                    user_key = user_info['key']
            if user_key is None:
                self.dvls_logger.error("[DvlsSDK.delete_user_by_name] - Deletion failed. User '" + username +
                                       "' not found", verbose_override)
            result = self._api.delete_user(user_key, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.delete_user_by_name] - Successful for " + username, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_user_by_name] - Failed for " + username, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_user_by_name] - No user logged in, aborting deletion of user " +
                                   username, verbose_override)
        return result

    def delete_user_by_id(self, user_id, verbose_override=None):
        """
        Deletes a user

        :param user_id: ID of the user to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.delete_user(user_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.delete_user_by_id] - Successful for " + str(user_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_user_by_id] - Failed for " + str(user_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_user_by_id] - No user logged in, aborting deletion of user " +
                                   str(user_id), verbose_override)
        return result

    def create_security_group(self, name, **options):
        """
        Create a security group

        :param name: Name of the security group to create
        :param options:
        - Description: description of the security group to create
        - verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': GroupInfoEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            if isinstance(name, str):
                if 'Description' in options:
                    if not isinstance(options.get('Description'), str):
                        self.dvls_logger.warning("[DvlsSDK.create_security_group] - Invalid description, ignoring",
                                               verbose_override)
                        del options['Description']
                options['Name'] = name
                options['ID'] = ''
                data_model = init_model('generated', 'SaveGroupInfoData')
                data_model.GroupInfo = init_model('generated', 'GroupInfoEntity')
                new_group = fill_data(data_model, options)
                result = self._api.create_security_group(new_group, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.create_security_group] - Successful for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.create_security_group] - Failed for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.create_security_group] - Name parameter must be a string, " +
                                       "aborting creation of security group " + name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_security_group] - No user logged in, aborting creation of " +
                                   "security group " + name, verbose_override)
        return result

    def get_security_group_by_name(self, name, verbose_override=None):
        """
        Get a security group using it's name

        :param name: Name of the security group to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': GroupInfoEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_security_group_by_name(name, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_security_group_by_name] - Successful for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_security_group_by_name] - Failed for " + name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_security_group_by_name] - No user logged in, " +
                                   "aborting get security group " + name, verbose_override)
        return result

    def get_security_group_by_id(self, sc_id, verbose_override=None):
        """
        Get a security group using it's id

        :param sc_id: Id of the security group to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': GroupInfoEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_security_group_by_id(sc_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_security_group_by_id] - Successful for " + str(sc_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_security_group_by_id] - Failed for " + str(sc_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_security_group_by_id] - No user logged in, " +
                                   "aborting get security group " + str(sc_id), verbose_override)
        return result

    def get_security_group_id(self, name, verbose_override=None):
        """
        Get the id of the security group with given name

        :param name: Name of the security group to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': Guid}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            group_result = self._api.get_security_group_by_name(name, verbose_override)
            if group_result.success:
                self.dvls_logger.info("[DvlsSDK.get_security_group_id] - Successful for " + name, verbose_override)
                group = group_result.data
                result.data = group['id']
            else:
                self.dvls_logger.error("[DvlsSDK.get_security_group_id] - Security Group '" + str(name) +
                                       "' not found, aborting get security group id", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_security_group_id] - No user logged in, aborting get " +
                                   "security group id for " + name, verbose_override)
        return result

    def get_security_group_tree(self, verbose_override=None):
        """
        Get the tree structure of security groups

        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': Tree structure of GroupInfoEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_security_groups_tree(verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_security_group_tree] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_security_group_tree] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_security_group_tree] - No user logged in, aborting get " +
                                   "security group tree", verbose_override)
        return result

    def modify_security_group_by_name(self, name, **options):
        """
        Modify a security group

        :param name: Name of the security group to modify
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        - Name: New name for the security group
        - Description: description of the security group to create
        :return: SDKResult{'data': GroupInfoEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            original_sec_result = self.get_security_group_id(name, verbose_override)
            if original_sec_result.success:
                sec_group_id = original_sec_result.data
                result = self.modify_security_group_by_id(sec_group_id, **options)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.modify_security_group_by_name] - Successful for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_security_group_by_name] - Failed for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.modify_security_group_by_name] - Could not find id for '" + name +
                                       "', aborting modification of security group", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_security_group_by_name] - No user logged in, " +
                                   "aborting modification of security group " + name, verbose_override)
        return result

    def modify_security_group_by_id(self, sc_id, **options):
        """
        Modify a security group

        :param sc_id: Id of the security group to modify
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        - Name: New name for the security group
        - Description: description of the security group to modify
        :return: SDKResult{'data': GroupInfoEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            existing_sec_result = self.get_security_group_by_id(sc_id, verbose_override)
            if existing_sec_result.success:
                existing_sec_group = existing_sec_result.data
                final_dict = DVLSConnection.object_to_flatten_dict(existing_sec_group, options)
                data_model = init_model('generated', 'SaveGroupInfoData')
                data_model.GroupInfo = init_model('generated', 'GroupInfoEntity')
                new_group = data_model
                new_group.GroupInfo = fill_data(data_model.GroupInfo, final_dict)
                new_group.OldName = existing_sec_group.get('name')
                result = self._api.modify_security_group(new_group, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.modify_security_group_by_id] - Successful for " + str(sc_id), verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_security_group_by_id] - Failed for " + str(sc_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.modify_security_group_by_id] - Could not get security group '" +
                                       str(sc_id) + "', aborting modification of security group", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_security_group_by_id] - No user logged in, " +
                                   "aborting modification of security group " + str(sc_id), verbose_override)
        return result

    def delete_security_group_by_name(self, name, verbose_override=None):
        """
        Deletes a security group

        :param name: Name of the security group to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            sc_result = self._api.get_security_group_by_name(name, verbose_override)
            if sc_result.success:
                sc_id = sc_result.data.get('id')
                result = self.delete_security_group_by_id(sc_id, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.delete_security_group_by_name] - Successful for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.delete_security_group_by_name] - Failed for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_security_group_by_name] - Could not get security group '" +
                                       str(name) + "', aborting deletion of security group", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_security_group_by_name] - No user logged in, " +
                                   "aborting deletion of security group " + name, verbose_override)
        return result

    def delete_security_group_by_id(self, sc_id, verbose_override=None):
        """
        Deletes a security group

        :param sc_id: Id of the security group to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.delete_security_group_by_id(sc_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.delete_security_group_by_id] - Successful for " + str(sc_id),
                                      verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_security_group_by_id] - Failed for " + str(sc_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_security_group_by_id] - No user logged in, " +
                                   "aborting deletion of security group " + str(sc_id), verbose_override)
        return result

    def create_role(self, name, **options):
        """
        Create a new role

        :param name: Name of the role to create
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': RoleEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            if isinstance(name, str):
                options['Name'] = name
                options['UserType'] = 1
                options['ID'] = ''
                data_model = init_model('generated', 'RoleEntity')
                new_role = fill_data(data_model, options)
                new_role.UserSecurity.AuthenticationType = 0
                result = self._api.create_role(new_role, verbose_override)
                if result.success:
                    if isinstance(result.data, dict) and 'key' in result.data:
                        result.data['id'] = result.data['key']
                    self.dvls_logger.info("[DvlsSDK.create_role] - Successful for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.create_role] - Failed for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.create_role] - Name must be a string, aborting creation of role " +
                                       name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_role] - No user logged in, aborting creation of role " +
                                   name, verbose_override)
        return result

    def get_role_by_name(self, name, verbose_override=None):
        """
        Get the role with given name

        :param name: Name of the role to get
        :param verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': RoleEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self.get_roles(verbose_override)
            if result.success:
                role = None
                roles = result.data
                for current_role in roles:
                    if current_role['display'] == name:
                        role = current_role
                        role['id']= role['key']
                        break
                if not role is None:
                    result.data = role
                    self.dvls_logger.info("[DvlsSDK.get_role_by_name] - Successful for " + name, verbose_override)
                else:
                    result.data = None
                    self.dvls_logger.error("[DvlsSDK.get_role_by_name] - Role '" + str(name) + "' not found", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_role_by_name] - Role '" + str(name) + "' not found", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_role_by_name] - No user logged in, aborting getrole " + name, verbose_override)
        return result

    def get_role_by_id(self, role_id, verbose_override=None):
        """
        Get the role with given id

        :param role_id: Id of the role to get
        :param verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': RoleEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self.get_roles(verbose_override)
            if result.success:
                role = None
                roles = result.data
                for current_role in roles:
                    if current_role['key'] == role_id:
                        role = current_role
                        role['id']= role['key']
                        break
                if not role is None:
                    result.data = role
                    self.dvls_logger.info("[DvlsSDK.get_role_by_id] - Successful for " + str(role_id), verbose_override)
                else:
                    result.data = None
                    self.dvls_logger.error("[DvlsSDK.get_role_by_id] - Role '" + str(role_id) + "' not found", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_role_by_id] - Role '" + str(role_id) + "' not found", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_role_by_id] - No user logged in, aborting get role " +
                                   str(role_id), verbose_override)
        return result

    def get_role_id(self, name, verbose_override=None):
        """
        Get the id of the role with given name

        :param name: Name of the role to get the id from
        :param verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': Guid}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            role_result = self.get_role_by_name(name, verbose_override)
            if role_result.success:
                role = role_result.data
                if not role is None:
                    result.data = role['key']
                    self.dvls_logger.info("[DvlsSDK.get_role_id] - Successful for " + str(name), verbose_override)
                else:
                    result.data = None
                    self.dvls_logger.error("[DvlsSDK.get_role_id] - Role '" + str(name) + "' not found", verbose_override)

            else:
                self.dvls_logger.error("[DvlsSDK.get_role_id] - Role '" + str(name) + "' not found", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_role_id] - No user logged in, aborting get role id for " +
                                   str(name), verbose_override)
        return result

    def get_roles(self, verbose_override=None):
        """
        Get all of the roles

        :param verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': RoleEntity[] (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_roles(verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_roles] - Successful", verbose_override)
                for r in result.data:
                    if isinstance(r, dict) and 'key' in r:
                        r['id'] = r['key']
            else:
                self.dvls_logger.error("[DvlsSDK.get_roles] - Could not get roles", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_roles] - No user logged in, aborting get roles", verbose_override)
        return result

    def modify_role_by_name(self, name, **options):
        """
        Modify the role with given name

        :param name: Name of the role to modify
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        - Name - New name to give to the role
        :return: SDKResult{'data': RoleEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            role_result = self.get_role_by_name(name, verbose_override)
            if role_result.success:
                role = role_result.data
                new_name = role.get('userSecurity').get('name')
                if 'Name' in options:
                    new_name = options.get('Name')
                options['FullName'] = options.get('Description')
                final_dict = DVLSConnection.object_to_flatten_dict(role, options)
                data_model = init_model('generated', 'RoleEntity')
                new_role = fill_data(data_model, final_dict)
                new_role.UserSecurity.ID = role['key']
                result = self._api.modify_role(new_role, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.modify_role_by_name] - Successful for " + name, verbose_override)
                    if isinstance(result.data, dict) and 'key' in result.data:
                        result.data['id'] = result.data['key']
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_role_by_name] - Could not get role '" + name +
                                           "', aborting modification", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.modify_role_by_name] - Modification failed for role '" + name +
                                       "'" , verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_role_by_name] - No user logged in, aborting modification of role " +
                                   name, verbose_override)
        return result

    def modify_role_by_id(self, role_id, **options):
        """
        Modify the role with given name

        :param role_id: Id of the role to modify
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        - Name - New name to give to the role
        :return: SDKResult{'data': RoleEntity (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            role_result = self.get_role_by_id(role_id, verbose_override)
            if role_result.success:
                role = role_result.data
                new_name = role.get('userSecurity').get('name')
                if 'Name' in options:
                    new_name = options.get('Name')
                options['FullName'] = options.get('Description')
                final_dict = DVLSConnection.object_to_flatten_dict(role, options)
                data_model = init_model('generated', 'RoleEntity')
                new_role = fill_data(data_model, final_dict)
                new_role.UserSecurity.ID = role['key']
                result = self._api.modify_role(new_role, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.modify_role_by_id] - Successful for " + str(role_id), verbose_override)
                    if isinstance(result.data, dict) and 'key' in result.data:
                        result.data['id'] = result.data['key']
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_role_by_id] - Modification failed for role '" +
                                           str(role_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.modify_role_by_id] - Could not get role '" + str(role_id) +
                                       "', aborting modification", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_role_by_id] - No user logged in, aborting modification of role " +
                                   str(role_id), verbose_override)
        return result

    def delete_role_by_name(self, name, verbose_override=None):
        """
        Delete the role with given name

        :param name: Name of the role to delete
        :param verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': RoleEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self.get_role_id(name, verbose_override)
            if result.success:
                role_id = result.data
                if role_id:
                    result = self._api.delete_role(role_id, verbose_override)
                    if result.success:
                        self.dvls_logger.info("[DvlsSDK.delete_role_by_name] - Successful for " + name, verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.delete_role_by_name] - Deletion failed for" + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.delete_role_by_name] - Could not get role id for '" + name +
                                           "', aborting deletion", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_role_by_name] - Could not get role id for '" + name +
                                       "', aborting deletion", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_role_by_name] - No user logged in, aborting deletion of role " +
                                   name, verbose_override)
        return result

    def delete_role_by_id(self, role_id, verbose_override=None):
        """
        Delete the role with given id

        :param role_id: Id of the role to delete
        :param verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': RoleEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.delete_role(role_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.delete_role_by_id] - Successful for " + str(role_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_role_by_id] - Deletion failed for " + str(role_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_role_by_id] - No user logged in, aborting deletion of role " +
                                   str(role_id), verbose_override)
        return result

    def create_password_template(self, mode, name, **options):
        """
        Create a new password template

        :param mode: generated\models\PasswordGeneratorMode
        :param name: Name of the new Password Template
        :param options:
        - verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            options['Name'] = name
            options['Mode'] = mode.value
            options_append = {}
            for option in options:
                if option.endswith("Min"):
                    if isinstance(options.get(option), int):
                        options_append['Include' + option[:-3]] = True
                    else:
                        options_append['Include' + option[:-3]] = False
            options.update(options_append)

            data_model = init_model('generated', 'PasswordConfiguration')
            new_pw_template = fill_data(data_model, options)
            result = self._api.create_password_template(new_pw_template, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.create_password_template] - Successful for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.create_password_template] - Creation failed for " + name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_password_template] - No user logged in, " +
                                   "aborting creation of password template " + name, verbose_override)
        return result

    def get_password_templates_by_name(self, name, verbose_override=None):
        """
        Get the password templates with given name

        :param name: Name of the Password Template to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PasswordConfiguration[] (as dictionary)}
        """
        result = SDKResult()
        templates = []
        if self._api.is_logged_on():
            pw_result = self.get_password_templates(verbose_override)
            if pw_result.success:
                pw_templates = pw_result.data
                for pw_template in pw_templates:
                    if pw_template['name'] == name:
                        #final_dict = self.object_to_flatten_dict(pw_template, {})
                        #data_model = init_model('generated', 'PasswordConfiguration')
                        #entry = fill_data(data_model, final_dict)
                        templates.append(pw_template)
                result.data = templates
                self.dvls_logger.info("[DvlsSDK.get_password_templates_by_name] - Successful for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_password_templates_by_name] - Password Template '" + str(name) +
                                       "' not found", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_password_templates_by_name] - No user logged in, " +
                                   "aborting get password template " + str(name), verbose_override)
        return result

    def get_password_template_by_id(self, pw_id, verbose_override=None):
        """
        Get the password template with given id

        :param pw_id: Id of the Password Template to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PasswordConfiguration (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            pw_result = self.get_password_templates(verbose_override)
            if pw_result.success:
                templates = pw_result.data
                for template in templates:
                    if 'id' in template and template.get('id') == pw_id:
                        #final_dict = self.object_to_flatten_dict(template, {})
                        #data_model = init_model('generated', 'PasswordConfiguration')
                        #entry = fill_data(data_model, final_dict)
                        result.data = template
                        break
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.get_password_template_by_id] - Successful for " + str(pw_id),
                                          verbose_override)
                else:
                    result.data = {}
                    self.dvls_logger.error("[DvlsSDK.get_password_template_by_id] - Password template " + str(pw_id) +
                                           " not found", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_password_template_by_id] - Password Template '" + str(pw_id) +
                                       "' not found", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_password_template_by_id] - No user logged in, " +
                                   "aborting get password template " + str(pw_id), verbose_override)
        return result

    def get_password_templates(self, verbose_override=None):
        """
        Get all Password Templates

        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PasswordConfiguration[] (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_password_templates(verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_password_templates] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_password_templates] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_password_templates] - No user logged in, " +
                                   "aborting get password templates", verbose_override)
        return result

    def modify_password_template(self, template_id, **options):
        """
        Modify a password template

        :param template_id: ID of the Password Template to modify
        :param options:
        - Mode - generated\models\PasswordGeneratorMode
        - verbose_override - If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            existing_template_result = self.get_password_template_by_id(template_id, verbose_override)
            if existing_template_result.success:
                existing_template = existing_template_result.data
                final_dict = DVLSConnection.object_to_flatten_dict(existing_template, options)
                if 'Mode' in final_dict:
                    final_dict['Mode'] = final_dict['Mode'].value
                options_append = {}
                for option in final_dict:
                    if option.endswith("Min"):
                        if isinstance(final_dict.get(option), int):
                            options_append['Include' + option[:-3]] = True
                        else:
                            options_append['Include' + option[:-3]] = False
                final_dict.update(options_append)
                data_model = init_model('generated', 'PasswordConfiguration')
                new_pw_template = fill_data(data_model, final_dict)
                result = self._api.modify_password_template(new_pw_template)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.modify_password_template] - Successful for " + str(template_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.modify_password_template] - Failed for " + str(template_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_password_template] - No user logged in, " +
                                   "aborting modification of password template " + str(template_id), verbose_override)
        return result

    def delete_password_template_by_id(self, template_id, verbose_override=None):
        """
        Delete the password template with given id

        :param template_id: Id of the Password Template to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            pw_templates_result = self.get_password_templates(verbose_override)
            if pw_templates_result.success:
                pw_templates = pw_templates_result.data
                for template in pw_templates:
                    if template.get('id') == template_id:
                        result = self._api.delete_password_template(template, verbose_override)
                        if result.success:
                            self.dvls_logger.info("[DvlsSDK.delete_password_template_by_id] - Successful for " +
                                                  str(template_id), verbose_override)
                        else:
                            self.dvls_logger.error("[DvlsSDK.delete_password_template_by_id] - Failed for " +
                                                   str(template_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_password_template_by_id] - Password template " +
                                       str(template_id) + " not found, cannot delete", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_password_template_by_id] - No user logged in, " +
                                   "aborting deletion of password template " + str(template_id), verbose_override)
        return result

    def get_features(self, verbose_override=None):
        """
        Get features

        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': FeaturesConfigurationEntity (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_features(verbose_override)
            if result.success:
                features_configuration_entity = init_model('generated', 'FeaturesConfigurationEntity')
                features = vars(fill_data(features_configuration_entity, result.data, True))
                result.data = features
                self.dvls_logger.info("[DvlsSDK.get_features] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_features] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_features] - No user logged in, aborting get features", verbose_override)
        return result

    def modify_features(self, **options):
        """
        Modify features

        :param options:
        - verbose_override: If provided will override the verbose setting of ApiManager
        - all properties of generated\models\FeaturesConfigurationEntity.py
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            features_result = self.get_features(verbose_override)
            if features_result.success:
                current_features = features_result.data
                final_dict = self.object_to_flatten_dict(current_features, options)
                features_configuration_entity = init_model('generated', 'FeaturesConfigurationEntity')
                features = fill_data(features_configuration_entity, final_dict)
                result = self._api.modify_features(features, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.modify_features] - Successful", verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_features] - Failed", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.modify_features] - Could not get current features, " +
                                       "aborting modification of features", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_features] - No user logged in, " +
                                   "aborting modification of features", verbose_override)
        return result

    def create_connection(self, entry_type, name, **options):
        """
        Create a connection

        :param entry_type: general\enums\ConnectionType
        :param name: Name of the connection entry to create
        :param options:
        - verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            if not isinstance(name, str):
                self.dvls_logger.error("[DvlsSDK.create_connection] - Name is not in string format, " +
                                       "aborting creation of connection entry", verbose_override)
            elif name == '':
                self.dvls_logger.error("[DvlsSDK.create_connection] - Empty name not allowed, " +
                                       "aborting creation of connection entry", verbose_override)
            else:
                if not isinstance(entry_type, str) and not isinstance(entry_type, ConnectionType):
                    self.dvls_logger.error("[DvlsSDK.create_connection] - Entry type is not in supported format, " +
                                           "aborting creation of connection entry " + name, verbose_override)
                else:
                    if isinstance(entry_type, str) and entry_type in self.STANDARD_ENTRY_TYPES:
                        type_id = ConnectionType.value_from_name(entry_type)
                    else:
                        type_id = entry_type.value
                        entry_type = ConnectionType(entry_type).name

                    if ConnectionType.valid_value(type_id):
                        entry = init_model('custom', 'PartialConnection')
                        entry = self._generate_connection_entry(entry, entry_type, type_id, name, options)
                        if entry is not None:
                            result = self._api.create_connection_entry(entry, verbose_override)
                            if result.success:
                                self.dvls_logger.info("[DvlsSDK.create_connection] - Successful for " + name, verbose_override)
                            else:
                                self.dvls_logger.error("[DvlsSDK.create_connection] - Failed for" + name, verbose_override)
                        else:
                            self.dvls_logger.error("[DvlsSDK.create_connection] - Error generating the entry to save, " +
                                                   "aborting creation of connection entry " + name, verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.create_connection] - Invalid connection type for " + name +
                                               ", aborting creation of connection entry", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_connection] - No user logged in, " +
                                   "aborting creation of connection entry " + name, verbose_override)
        return result

    def get_connections_by_name(self, name, repository_id, verbose_override=None):
        """
        Gets all connections that have the given name in repository

        :param repository_id: Id of the repository to get connections from
        :param name: Name of the connections you want to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection[] (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            rep_result = self.get_repository_entries_list(repository_id, verbose_override)
            if rep_result.success:
                entries = rep_result.data
                entries = DVLSConnection._extract_entries_with_name(name, entries)
                result.data = []
                if len(entries) <= 0:
                    result.result = 0
                for entry in entries:
                    full_entry_result = self.get_connection_by_id(entry.get('id'), verbose_override)
                    if full_entry_result.success:
                        result.data.append(full_entry_result.data)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_connections_by_name] - Successful for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_connections_by_name] - Failed for " + name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_connections_by_name] - No user logged in, " +
                                   "aborting get connections with name " + name, verbose_override)
        return result

    def get_connection_by_id(self, connection_id, verbose_override=None):
        """
        Get connection with given id

        :param connection_id: Id of the connection to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_connection_by_id(connection_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_connection_by_id] - Successful for " + str(connection_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_connection_by_id] - Failed for " + str(connection_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_connection_by_id] - No user logged in, " +
                                   "aborting get connection " + connection_id, verbose_override)
        return result

    def get_connection_sensitive_data(self, connection_id, verbose_override=None):
        """
        Used to get sensitive information on an entry

        :param connection_id: Id of the connection to get sensitive data for
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': { 'credentialConnectionId': string,
                                     'credentials': {'domain': string, 'password': string, 'userName': string},
                                     'gatewayCredentialConnectionID': string,
                                     'passwordItem': SensitiveItem,
                                     'redirectDirectX': bool} (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_sensitive_data(connection_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_connection_sensitive_data] - Successful for " + str(connection_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_connection_sensitive_data] - Failed for " + str(connection_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_connection_sensitive_data] - No user logged in, " +
                                   "aborting get sensitive data for " + connection_id, verbose_override)
        return result

    def get_connection_password(self, connection_id, verbose_override=None):
        """
        Get password for connection with given id

        :param connection_id: Id of the connection to get the password from
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': string}
        """
        result = self.get_connection_sensitive_data(connection_id, verbose_override)
        if result.success:
            sensitive_data = result.data
            result.data = sensitive_data.get('passwordItem').get('sensitiveData')
            self.dvls_logger.info("[DvlsSDK.get_connection_password] - Successful for " + str(connection_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_connection_password] - Failed for " + str(connection_id), verbose_override)
        return result

    def modify_connection_by_id(self, entry_type, connection_id, **options):
        """
        Modify a connection with given id

        :param entry_type: general\enums\ConnectionType
        :param connection_id: Id of the connection entry to modify
        :param options:
        - verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            if not isinstance(entry_type, str) and not isinstance(entry_type, ConnectionType):
                self.dvls_logger.error("[DvlsSDK.modify_connection_by_id] - Entry type is not in supported format, " +
                                       "aborting modification of connection entry " + str(connection_id), verbose_override)
            else:
                if isinstance(entry_type, str) and entry_type in self.STANDARD_ENTRY_TYPES:
                    type_id = ConnectionType.value_from_name(entry_type)
                else:
                    type_id = entry_type.value
                    entry_type = ConnectionType(entry_type).name

                if ConnectionType.valid_value(type_id):
                    entry_result = self.get_connection_by_id(connection_id, verbose_override)
                    if entry_result.success:
                        entry = entry_result.data
                        new_name = entry['name']
                        if 'Name' in options:
                            new_name = options['Name']
                        options['Id'] = entry['id']
                        final_dict = self.object_to_flatten_dict(entry, options)
                        partial_entry = init_model('custom', 'PartialConnection')
                        created_entry = self._generate_connection_entry(partial_entry, entry_type, type_id, new_name, final_dict)

                        result = self._api.modify_connection_entry(created_entry, verbose_override)
                        if result.success:
                            self.dvls_logger.info("[DvlsSDK.modify_connection_by_id] - Successful for " +
                                                  str(connection_id), verbose_override)
                        else:
                            self.dvls_logger.error("[DvlsSDK.modify_connection_by_id] - Failed for " +
                                                   str(connection_id), verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.modify_connection_by_id] - Could not get connection entry, " +
                                               "aborting modification of connection entry " + str(connection_id), verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_connection_by_id] - Invalid connection type, " +
                                           "aborting modification of connection entry " + str(connection_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_connection_by_id] - No user logged in, " +
                                   "aborting modification of connection entry " + str(connection_id), verbose_override)
        return result

    def delete_connection_by_id(self, connection_id, verbose_override=None):
        """
        Delete connection with given id

        :param connection_id: Id of the connection to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        return self.delete_entry_by_id(connection_id, verbose_override)

    def create_credential_entry(self, entry_type, name, **options):
        """
        Create a new credential entry

        :param entry_type: A valid CREDENTIAL_ENTRY_TYPES value
        :param name: Name of the new credential entry
        :param options:
        - verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            if not isinstance(name, str):
                self.dvls_logger.error("[DvlsSDK.create_credential_entry] - Name is not in string format, " +
                                       "aborting creation of credential entry", verbose_override)
            elif name == '':
                self.dvls_logger.error("[DvlsSDK.create_credential_entry] - Empty name not allowed, " +
                                       "aborting creation of credential entry", verbose_override)
            else:
                if entry_type in self.CREDENTIAL_ENTRY_TYPES or entry_type == "Credential":
                    type_id = ConnectionType.value_from_name("Credential")
                    options['ConnectionSubType'] = entry_type
                    entry = init_model('custom', 'PartialConnection')
                    entry = fill_data(entry, options)
                    entry.Security.Permissions = []
                    entry.Name = name
                    entry.ConnectionType = type_id
                    security_role_right = init_enum(
                        'generated', 'SecurityRoleRight')
                    if 'RoleOverride' not in options:
                        set_role_override = False
                        if 'ViewRoles' in options:
                            entry.Security.ViewOverride = 1
                            set_role_override = True
                        for item, value in security_role_right.__members__.items():
                            if item in options:
                                set_role_override = True
                                options['Right'] = item
                                if isinstance(options[item], list):
                                    options['RoleValues'] = str(
                                        options[item])[1:-1]
                                    options['Override'] = 'Custom'
                                else:
                                    options['RoleValues'] = ''
                                    options['Override'] = options[item]
                                connection_permission = init_model(
                                    'generated', 'ConnectionPermission')
                                entry.Security.Permissions.append(fill_data(connection_permission, options))
                        if set_role_override:
                            entry.Security.RoleOverride = 1
                    else:
                        role_override = options.get('RoleOverride')
                        if role_override == 'Default' \
                                or role_override == 'Never' \
                                or role_override == 'Everyone':
                            conflict = False
                            if 'ViewRoles' in options:
                                conflict = True
                            else:
                                for item in security_role_right.__members__.items():
                                    if item in options:
                                        conflict = True
                            if conflict:
                                self.dvls_logger.error("[DvlsSDK.create_credential_entry] - RoleOverride must be " +
                                                       "omitted in order to use custom values. Aborting entry creation",
                                                       verbose_override)
                                return SDKResult(result)
                        else:
                            self.dvls_logger.error("[DvlsSDK.create_credential_entry] - Incorrect value '" +
                                                   role_override + "' for RoleOverride", verbose_override)
                    if 'SecurityGroup' in options:
                        sc_result = self.get_security_group_id(options['SecurityGroup'], verbose_override)
                        if sc_result.success:
                            entry.SecurityGroupId = sc_result.data
                    if entry_type == 'Default':
                        data_model = init_model('generated', 'CredentialUsernamePassword')
                    else:
                        data_model = init_model('generated', 'Credential' + entry_type)
                    data = fill_data(data_model, options)
                    entry.data = bytes.decode(
                        binascii.hexlify(
                            self._api.EncryptionManager.aes_encrypt(json.dumps(data, cls=Encoder))))
                    if 'Id' in options:
                        result = self._api.modify_credential_entry(entry, verbose_override)
                    else:
                        result = self._api.create_credential_entry(entry, verbose_override)
                    if result.success:
                        self.dvls_logger.info("[DvlsSDK.create_credential_entry] - Successful for " + name, verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.create_credential_entry] - Failed for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.create_credential_entry] - Entry_type must be of a type in " +
                                           "CREDENTIAL_ENTRY_TYPES , aborting creation of credential entry " + name,
                                            verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_credential_entry] - No user logged in, " +
                                   "aborting creation of credential entry " + name, verbose_override)
        return result

    def get_credential_entries_by_name(self, name, repository_id, verbose_override=None):
        """
        Gets all credential entries that have the given name in repository

        :param repository_id: Id of the repository to get entries from
        :param name: Name of the credential entries you want to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection[] (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            rep_result = self.get_repository_entries_tree(repository_id, verbose_override)
            if rep_result.success:
                entries = rep_result.data
                filtered_entries = DVLSConnection._extract_entries_with_name(name, entries)
                filtered_entries = DVLSConnection._extract_entries_with_type(ConnectionType.Credential.value, filtered_entries)
                result.data = []
                for cred in filtered_entries:
                    full_entry_result = self.get_connection_by_id(cred.get('id'), verbose_override)
                    if full_entry_result.success:
                        result.data.append(full_entry_result.data)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.get_credential_entries_by_name] - Successful for " + name,
                                          verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.get_credential_entries_by_name] - Failed for " + name,
                                           verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_credential_entries_by_name] - No user logged in, " +
                                   "aborting get credential entries with name " + name, verbose_override)
        return result

    def get_credential_entry_by_id(self, cred_id, verbose_override=None):
        """
        Get credential with given id

        :param cred_id: Id of the credential to get
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_connection_by_id(cred_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_credential_entry_by_id] - Successful for " + str(cred_id),
                                      verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_credential_entry_by_id] - Failed for " + str(cred_id),
                                       verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_credential_entry_by_id] - No user logged in, " +
                                   "aborting get credential entry " + cred_id, verbose_override)
        return result

    def modify_credential_entry(self, entry_type, cred_id, **options):
        """
        Modify a credential entry

        :param entry_type: A valid CREDENTIAL_ENTRY_TYPES value
        :param cred_id: Id of the credential entry to modify
        :param options:
        - verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            con_result = self.get_connection_by_id(cred_id, verbose_override)
            if con_result.success:
                entry = con_result.data
                options['Id'] = entry['id']
                new_name = entry['name']
                if 'name' in options:
                    new_name = options['name']
                result = self.create_credential_entry(entry_type, new_name, **options)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.modify_credential_entry] - Successful for " + str(cred_id),
                                          verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_credential_entry] - Failed for " + str(cred_id),
                                           verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.modify_credential_entry] - Could not get credential entry, " +
                                       "aborting modification of credential entry " + str(cred_id), verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_credential_entry] - No user logged in, " +
                                   "aborting modification of credential entry " + str(cred_id), verbose_override)
        return result

    def delete_credential_entry_by_id(self, cred_id, verbose_override=None):
        """
        Delete credential entry with given id

        :param cred_id: Id of the credential entry to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = self.delete_entry_by_id(cred_id, verbose_override)
        if result.success:
            self.dvls_logger.info("[DvlsSDK.delete_credential_entry_by_id] - Successful for " + str(cred_id),
                                  verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_credential_entry_by_id] - Failed for " + str(cred_id),
                                   verbose_override)
        return result

    def delete_entry_by_id(self, entry_id, verbose_override=None):
        """
        Delete entry with given id

        :param entry_id: Id of the entry to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            con_result = self.get_connection_by_id(entry_id, verbose_override)
            if con_result.success:
                entry = con_result.data
                if entry['connectionType'] != 92:
                    result = self._api.delete_entry(entry['name'], entry, verbose_override)
                    if result.success:
                        self.dvls_logger.info("[DvlsSDK.delete_entry_by_id] - Successful for " + str(entry_id),
                            verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.delete_entry_by_id] - Failed for " + str(entry_id),
                                               verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.delete_entry_by_id] - Root entry deletion denied", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_entry_by_id] - Entry '" + str(entry_id) +
                                       "' not found, deletion failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_entry_by_id] - No user logged in, " +
                                   "aborting deletion of entry " + str(entry_id), verbose_override)
        return result

    def create_private_vault_entry(self, entry_type, name, **options):
        """
        Create a private vault entry

        :param entry_type: general\enums\ConnectionType
        :param name: Name of the connection entry to create
        :param options:
        - verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        verbose_override = self.extract_verbose_override_option(options)
        options['IsPrivate'] = "true"
        result = self.create_connection(entry_type, name, **options)
        if result.success:
            self.dvls_logger.info("[DvlsSDK.create_private_vault_entry] - Successful for " + name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_private_vault_entry] - Failed for " + name, verbose_override)
        return result

    def get_private_vault_entries_tree(self, verbose_override=None):
        """
        Get tree structure of private vault entries

        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_private_vault_entries(verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_private_vault_entries_tree] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_private_vault_entries_tree] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_private_vault_entries_tree] - No user logged in, " +
                                   "aborting get private vault tree", verbose_override)
        return result

    def get_private_vault_entries_list(self, verbose_override=None):
        """
        Get list of private vault entries

        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection[] (as dictionary)}
        """
        result = self.get_private_vault_entries_tree(verbose_override)
        if result.success:
            entries = result.data
            result.data = self._get_entries_list(entries)
            self.dvls_logger.info("[DvlsSDK.get_private_vault_entries_list] - Successful", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_private_vault_entries_list] - Failed", verbose_override)
        return result

    def get_private_vault_entries_by_name(self, name, verbose_override=None):
        """
        Get private vault entries that have the given name

        :param name: Name of the entries to find
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection[] (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self.get_private_vault_entries_tree(verbose_override)
            if result.success:
                entries = result.data
                result.data = DVLSConnection._extract_entries_with_name(name, entries)
                self.dvls_logger.info("[DvlsSDK.get_private_vault_entries_by_name] - Successful for " + name, verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_private_vault_entries_by_name] - Failed for " + name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_private_vault_entries_by_name] - No user logged in, " +
                                   "aborting get private vault entries with name " + name, verbose_override)
        return result

    def get_private_vault_entry_by_id(self, entry_id, verbose_override=None):
        """
        Get private vault entry with the given id

        :param entry_id: Id of the entry to find
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self.get_private_vault_entries_tree(verbose_override)
            if result.success:
                entries = result.data
                result = DVLSConnection._extract_entry_with_id(entry_id, entries)
                self.dvls_logger.info("[DvlsSDK.get_private_vault_entry_by_id] - Successful for " + str(entry_id),
                                      verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_private_vault_entry_by_id] - Failed for " + str(entry_id),
                                       verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_private_vault_entry_by_id] - No user logged in, " +
                                   "aborting get private vault entry " + str(entry_id), verbose_override)
        return result

    def modify_private_vault_entry_by_id(self, entry_type, entry_id, **options):
        """
        Modify a private vault entry with given id

        :param entry_type: general\enums\ConnectionType
        :param entry_id: Id of the private entry to modify
        :param options:
        - verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        options['IsPrivate'] = "true"
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            if not isinstance(entry_type, str) and not isinstance(entry_type, ConnectionType):
                self.dvls_logger.error("[DvlsSDK.modify_private_vault_entry_by_id] - Entry type is not in supported " +
                                       "format, aborting modification of private vault entry " + str(entry_id),
                                        verbose_override)
            else:
                if isinstance(entry_type, str) and entry_type in self.STANDARD_ENTRY_TYPES:
                    type_id = ConnectionType.value_from_name(entry_type)
                else:
                    type_id = entry_type.value
                    entry_type = ConnectionType(entry_type).name

                if ConnectionType.valid_value(type_id):
                    entry_result = self.get_private_vault_entry_by_id(entry_id, verbose_override)
                    if entry_result.success:
                        entry = entry_result.data
                        new_name = entry['name']
                        if 'Name' in options:
                            new_name = options['Name']
                        options['Id'] = entry['id']
                        final_dict = self.object_to_flatten_dict(entry, options)
                        partial_entry = init_model('custom', 'PartialConnection')
                        created_entry = self._generate_connection_entry(partial_entry, entry_type, type_id,
                                                                        new_name, final_dict)

                        result = self._api.modify_connection_entry(created_entry, verbose_override)
                        if result.success:
                            self.dvls_logger.info("[DvlsSDK.modify_private_vault_entry_by_id] - Successful for " +
                                                  str(entry_id), verbose_override)
                        else:
                            self.dvls_logger.error("[DvlsSDK.modify_private_vault_entry_by_id] - Failed for " +
                                                   str(entry_id), verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.modify_private_vault_entry_by_id] - Could not get " +
                                               "entry, aborting modification of private vault entry " + str(entry_id),
                                               verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.modify_private_vault_entry_by_id] - Invalid connection type, " +
                                           "aborting modification of private vault entry " + str(entry_id),
                                           verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.modify_private_vault_entry_by_id] - No user logged in, " +
                                   "aborting modification of private vault entry " + str(entry_id), verbose_override)
        return result

    def delete_private_vault_entry_by_id(self, entry_id, verbose_override=None):
        """
        Delete private vault entry with the given id

        :param entry_id: Id of the private vault entry to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            entry_result = self.get_private_vault_entry_by_id(entry_id, verbose_override)
            if entry_result.success:
                entry = entry_result.data
                result = self._api.delete_private_vault_entry(entry_id, entry, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.delete_private_vault_entry_by_id] - Successful for " +
                                          str(entry_id), verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.delete_private_vault_entry_by_id] - Failed for " +
                                           str(entry_id), verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.delete_private_vault_entry_by_id] - Could not get private" +
                                       " vault entry " + str(entry_id) + ", aborting deletion", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_private_vault_entry_by_id] - No user logged in, " +
                                   "aborting deletion of private vault entry " + str(entry_id), verbose_override)
        return result

    def create_repository(self, name, **options):
        """
        Create a repository

        :param name: Name of the repository to create
        :param options:
        - Description: description of the repository to create
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        verbose_override = self.extract_verbose_override_option(options)
        if self._api.is_logged_on():
            if isinstance(name, str):
                response = self.get_repository_id(name, verbose_override)
                if response.data is None:
                    if 'Description' in options:
                        if not isinstance(options.get('Description'), str):
                            self.dvls_logger.warning("[DvlsSDK.create_repository] - Invalid description, ignoring",
                                                     verbose_override)
                            del options['Description']
                    options['Name'] = name
                    options['ID'] = self._create_uuid()
                    data_model = init_model('generated', 'RepositoryEntity')
                    new_repo = fill_data(data_model, options)
                    result = self._api.create_repository(new_repo, verbose_override)
                    if result.success:
                        self.dvls_logger.info("[DvlsSDK.create_repository] - Successful for " + name, verbose_override)
                    else:
                        self.dvls_logger.error("[DvlsSDK.create_repository] - Failed for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.create_repository] - Repository '" + name +
                                           "' already exists", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.create_repository] - Name must be a string, " +
                                       "aborting creation of repository " + name, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.create_repository] - No user logged in, " +
                                   "aborting creation of repository " + name, verbose_override)
        return result

    def change_repository(self, name, verbose_override=None):
        """
        Change the currently active repository

        :param name: Name of the repository to create
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            repo_id = ''
            if name == 'Default':
                repo_id = self.DEFAULT_REPO_GUID
            else:
                result = self.get_repository_id(name, verbose_override)
                if result.success:
                    repo_id = result.data
                    self.dvls_logger.info("[DvlsSDK.change_repository] - Successful for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.change_repository] - Failed for " + name, verbose_override)
            result = self._api.change_active_repository(repo_id, verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.change_repository] - No user logged in, " +
                                   "aborting changing repository to " + name, verbose_override)
        return result

    def get_repository_entries_tree(self, repository_id, verbose_override=None):
        """
        Get tree structure of all entries of repository

        :param repository_id: Id of the repository to get entries from
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result= self._api.get_active_repository_entries(repository_id, verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_repository_entries_tree] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_repository_entries_tree] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_repository_entries_tree] - No user logged in, " +
                                   "aborting get current repository entries tree", verbose_override)
        return result

    def get_repository_entries_list(self, repository_id, verbose_override=None):
        """
        Get list of all entries of repository

        :param repository_id: Id of the repository to get entries from
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': PartialConnection[] (as dictionary)}
        """
        result = self.get_repository_entries_tree(repository_id, verbose_override)
        if result.success:
            entries = result.data
            entries = self._get_entries_list(entries)
            result.data = []
            for entry in entries:
                full_entry_result = self.get_connection_by_id(entry.get('id'), verbose_override)
                if full_entry_result.success:
                    result.data.append(full_entry_result.data)
        if result.success:
            self.dvls_logger.info("[DvlsSDK.get_repository_entries_list] - Successful", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_repository_entries_list] - Failed", verbose_override)
        return result

    def get_repository_id(self, name, verbose_override=None):
        """
        Get id of the repository with the given name

        :param name: Name of the repository to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': string}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            repositories_result = self.get_repositories(verbose_override)
            if repositories_result.success:
                repositories = repositories_result.data
                for repo in repositories:
                    if repo['name'] == name:
                        result.data = repo['idString']
                        break
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.get_repository_id] - Successful for " + name, verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.get_repository_id] - Repository '" + name +
                                           "' not found", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_repository_id] - No user logged in, " +
                                   "aborting get id of repository " + name, verbose_override)
        return result

    def get_repositories(self, verbose_override=None):
        """
        Get list of all repositories for user logged in

        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': RepositoryEntity[] (as dictionary)}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            result = self._api.get_repositories(verbose_override)
            if result.success:
                self.dvls_logger.info("[DvlsSDK.get_repositories] - Successful", verbose_override)
            else:
                self.dvls_logger.error("[DvlsSDK.get_repositories] - Failed", verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.get_repositories] - No user logged in, " +
                                   "aborting get repositories", verbose_override)
        return result

    def delete_repository_by_name(self, name, verbose_override=None):
        """
        Delete repository with the given name

        :param name: Name of the repository to delete
        :param verbose_override: If provided will override the verbose setting of ApiManager
        :return: SDKResult{'data': None}
        """
        result = SDKResult()
        if self._api.is_logged_on():
            repo_id = None
            result = self.get_repository_id(name, verbose_override)
            if result.success:
                repo_id = result.data
            if not repo_id is None:
                result = self._api.delete_repository_by_id(repo_id, verbose_override)
                if result.success:
                    self.dvls_logger.info("[DvlsSDK.delete_repository_by_name] - Successful for " + name,
                                          verbose_override)
                else:
                    self.dvls_logger.error("[DvlsSDK.delete_repository_by_name] - Failed for " + name,
                                           verbose_override)
        else:
            self.dvls_logger.error("[DvlsSDK.delete_repository_by_name] - No user logged in, " +
                                   "aborting deletion of repository " + name, verbose_override)
        return result

    @staticmethod
    def _extract_entry_with_id(connection_id, entries):
        result = SDKResult()
        if not isinstance(entries, list):
            entries = [entries]
        for entry in entries:
            if 'partialConnections' in entry:
                if entry['partialConnections']:
                    result = DVLSConnection._extract_entry_with_id(connection_id, entry['partialConnections'])
            if not result.success and 'id' in entry:
                if entry['id'] == connection_id:
                    result.data = entry
                    break
        return result

    @staticmethod
    def _get_entries_list(entries, entries_list=None):
        if entries_list is None:
            entries_list = []
        if not isinstance(entries, list):
            entries = [entries]
        for e in entries:
            if 'partialConnections' in e:
                if e['partialConnections']:
                    entries_list = DVLSConnection._get_entries_list(e['partialConnections'], entries_list)
                    entries_list.append(e)
                else:
                    entries_list.append(e)
        return entries_list

    @staticmethod
    def _extract_entries_with_name(name, entries):
        entries_found = []
        if not isinstance(entries, list):
            entries = [entries]
        for entry in entries:
            if 'partialConnections' in entry:
                if entry['partialConnections']:
                    entries_found.extend(DVLSConnection._extract_entries_with_name(name, entry['partialConnections']))
            if 'name' in entry:
                if entry['name'] == name:
                    entries_found.append(entry)
        return entries_found

    @staticmethod
    def _extract_entries_with_type(entry_type, entries):
        entries_found = []
        for entry in entries:
            if 'partialConnections' in entry:
                if entry['partialConnections']:
                    entries_found.extend(DVLSConnection._extract_entries_with_type(entry_type, entry['partialConnections']))
            if 'connectionType' in entry:
                if isinstance(entry_type, dict):
                    if entry['connectionType'] in entry_type:
                        entries_found.append(entry)
                else:
                    if entry['connectionType'] == entry_type:
                        entries_found.append(entry)
        return entries_found

    # Used to creata a unique GUID
    @staticmethod
    def _create_uuid():
        new_uuid = str(uuid.uuid4())
        return new_uuid

    # Used to fetch server informations. Mostly used to get the RSA public key

    @staticmethod
    def _flatten_entry(entry_dict):
        acc = {}
        for key, value in entry_dict.items():
            if isinstance(value, dict):
                res = DVLSConnection._flatten_entry(value)
                acc = dict(acc, **res)
            else:
                if not key == 'username':
                    acc[key] = value
        return copy.deepcopy(acc)

    @staticmethod
    def _toUpperFirstLetter(entry_dict):
        acc = {}
        upper = lambda s: s[:1].upper() + s[1:] if s else ''
        for key, value in entry_dict.items():
            key = upper(key)
            acc[key] = value
        return copy.deepcopy(acc)

    def _generate_connection_entry(self, entry, entry_type, entry_type_id, name, options):
        verbose_override = self.extract_verbose_override_option(options)
        options['SecurityRoleRight'] = init_enum('generated', 'SecurityRoleRight')

        ConnectionValidation.sanitize_options(entry, options)
        entry = fill_data(entry, options)
        entry.Security.Permissions = []
        entry.Name = name
        entry.ConnectionType = entry_type_id

        if 'SecurityGroup' in options:
            sg_result = self.get_security_group_id(options['SecurityGroup'])
            if sg_result.success:
                entry.SecurityGroupId = sg_result.data

        if entry_type_id == ConnectionType.Root.value or entry_type_id == ConnectionType.Credential.value:
            self.dvls_logger.error("Cannot generate a root connection or credential", verbose_override)
            return None

        if entry_type_id == ConnectionType.Group.value:
            data_model = init_model('generated', 'SaveGroupInfoData')
            data_model.GroupInfo = init_model('generated', 'GroupInfoEntity')
        elif entry_type_id == ConnectionType.SSHTunnel.value or entry_type_id == ConnectionType.SSHShell.value:
            data_model = init_model('generated', 'TerminalEntry')
            private_key_type = options.get('PrivateKeyType')
            private_key_id = options.get('PrivateKeyConnectionID')
            if private_key_id:
                if private_key_type != 'Link' and private_key_type != 'PrivateVault':
                    self.dvls_logger.error("Private Key type missing for Private Key ID: "
                                           "possible values: 'Link' or 'PrivateVault'", verbose_override)
                    return None
            else:
                if private_key_type == 'PrivateVault' or private_key_type == 'Link':
                    self.dvls_logger.error("Please specify the name of the Private Key", verbose_override)
                elif private_key_type == 'File':
                    if 'PrivateKeyFileName' not in options:
                        self.dvls_logger.error("Please specify the Private Key file", verbose_override)
                elif private_key_type == 'Data':
                    if 'PrivateKeyData' not in options:
                        self.dvls_logger.error("Please specify the Private Key data", verbose_override)
                elif private_key_type == 'Personal':
                    options['PrivateKeyType'] = 'MyDefault'
            ssh_private_key_type = options.get('SSHGatewayPrivateKeyType')
            ssh_private_key_id = options.get('SSHGatewayPrivateKeyConnectionID')
            if ssh_private_key_id:
                if ssh_private_key_type != 'Link' and ssh_private_key_type != 'PrivateVault':
                    self.dvls_logger.error("Private Key type missing for Private Key ID: possible values:"
                                           " 'Link' or 'PrivateVault'", verbose_override)
            else:
                if ssh_private_key_type == 'PrivateVault' or ssh_private_key_type == 'Link':
                    self.dvls_logger.error("Please specify the name of the Private Key", verbose_override)
                elif ssh_private_key_type == 'File':
                    if 'PrivateKeyFileName' not in options:
                        self.dvls_logger.error("Please specify the Private Key file", verbose_override)
                elif ssh_private_key_type == 'Data':
                    if 'PrivateKeyData' not in options:
                        self.dvls_logger.error("Please specify the Private Key data", verbose_override)
                elif ssh_private_key_type == 'Personal':
                    options['SSHGatewayPrivateKeyType'] = 'MyDefault'
            ssh_gw_cred_con_id = options.get('SSHGatewayCredentialConnectionID')
            ssh_gw_cred_con_src = options.get('SSHGatewayCredentialSource')
            if ssh_gw_cred_con_src == 'Prompt' and ssh_gw_cred_con_id:
                self.dvls_logger.error("SSH Gateway Credentials conflict (use prompt and specified): "
                                       "credentials will not be set.", verbose_override)
            else:
                if ssh_gw_cred_con_id:
                    options['SSHGatewayCredentialSource'] = 'CredentialRepository'
                if ssh_gw_cred_con_src == 'Prompt':
                    options['SSHGatewayCredentialConnectionID'] = self.GWCCID_UseCredRepoPrompt
        else:
            data_model = init_model('generated', entry_type + 'Entry')
        data = fill_data(data_model, options)
        if entry_type_id == ConnectionType.RDPConfigured.value:
            if 'GatewayProfileUsageMethod' in options:
                if options['GatewayProfileUsageMethod'] == 'Explicit' and 'GatewayUsageMethod' in options:
                    if options['GatewayUsageMethod'] == 'ProxyModeDetect' or options['GatewayUsageMethod'] == 'ModeDirect':
                        flag = 0
                        if 'GatewayUserName' in options or 'GatewayPassword' in options:
                            flag += 1
                        if 'GatewayPrivateVaultSearchString' in options:
                            data.GatewayCredentialConnectionID = self.GWCCID_UsePrvVltSrch
                            flag += 1
                        if options.get('GatewayUseCredRepoPrompt'):
                            data.GatewayCredentialConnectionID = self.GWCCID_UseCredRepoPrompt
                            flag += 1
                        if options.get('GatewayUsePersoCred'):
                            data.GatewayCredentialConnectionID = self.GWCCID_UsePersoCred
                            flag += 1
                        if 'GatewayCredentialConnectionID' in options:
                            data.GatewayCredentialConnectionID = options['GatewayCredentialConnectionID']
                            flag += 1
                        if flag > 1:
                            self.dvls_logger.error('Too many RDP gateway credentials specified, '
                                                   'aborting entry creation', verbose_override)
                            return None
            if 'RdpVersion' in options:
                rdp_version = init_enum('generated', 'RDPVersion')
                data.version = rdp_version.value_from_name(options['RdpVersion'])
            if 'WinPostStr' in options:
                data.winposstr = options['WinPostStr']
                data.useWinposstr = True
        if entry_type_id == ConnectionType.SSHTunnel.value:
            data_model = init_model('generated', 'PortForward')
            data_model = fill_data(data_model, options)
            data.PortForwards = [data_model]
        if 'Password' in options:
            if isinstance(options['Password'], str):
                data.PasswordItem.HasSensitiveData = True
                data.PasswordItem.SensitiveData = options['Password']
        if 'RunAsPasswordItem' in data.__dict__:
            if 'RunAsPassword' in options:
                data.RunAsPasswordItem.hasSensitiveData = True
                data.RunAsPasswordItem.SensitiveData = options['RunAsPassword']
            else:
                data.RunAsPasswordItem.hasSensitiveData = False
        if 'PrivateKeyPassPhraseItem' in data.__dict__:
            if 'PrivateKeyPassphrase' in options:
                data.PrivateKeyPassPhraseItem.hasSensitiveData = True
                data.PrivateKeyPassPhraseItem.SensitiveData = options['PrivateKeyPassphrase']
            else:
                data.PrivateKeyPassPhraseItem.hasSensitiveData = False
        if 'SSHGatewayPrivateKeyPassPhraseItem' in data.__dict__:
            if 'SSHGatewayPrivateKeyPassphrase' in options:
                data.SSHGatewayPrivateKeyPassPhraseItem.hasSensitiveData = True
                data.SSHGatewayPrivateKeyPassPhraseItem.SensitiveData = options[
                    'SSHGatewayPrivateKeyPassphrase']
            else:
                data.SSHGatewayPrivateKeyPassPhraseItem.hasSensitiveData = False
        if 'ProxyPasswordItem' in data.__dict__:
            if 'ProxyPassword' in options:
                data.ProxyPasswordItem.hasSensitiveData = True
                data.ProxyPasswordItem.SensitiveData = options['ProxyPassword']
            else:
                data.ProxyPasswordItem.hasSensitiveData = False
        if 'SSHGatewayPasswordItem' in data.__dict__:
            if 'SSHGatewayPassword' in options:
                data.SSHGatewayPasswordItem.hasSensitiveData = True
                data.SSHGatewayPasswordItem.SensitiveData = options['SSHGatewayPassword']
            else:
                data.SSHGatewayPasswordItem.hasSensitiveData = False
        entry.data = bytes.decode(binascii.hexlify(self._api.EncryptionManager.aes_encrypt(json.dumps(data, cls=Encoder))))
        return entry

    def _generate_user_entity(self, user_info, options, verbose_override=None):
        new_user = None
        if 'Password' in options:
            if 'AuthenticationType' in options:
                if options['AuthenticationType'] == 'Domain':
                    self.dvls_logger.warning("Ignoring password data. Domain users do not need to set a password",
                                             verbose_override)
                elif options['AuthenticationType'] == 'SqlServer' or options['AuthenticationType'] == 'Builtin':
                    options['Password'] = bytes.decode(
                        binascii.hexlify(
                            self._api.EncryptionManager.aes_encrypt(options['Password'])))
            else:
                options['Password'] = bytes.decode(
                    binascii.hexlify(
                        self._api.EncryptionManager.aes_encrypt(options['Password'])))
        else:
            if 'AuthenticationType' in options and (
                    options['AuthenticationType'] == 'Builtin' or options['AuthenticationType'] == 'SqlServer'):
                self.dvls_logger.error(
                    "Password required to create Custom users, aborting creation of user " + username, verbose_override)
                return new_user
        if 'CustomRoles' in options:
            option_roles = options.get('CustomRoles')
            rids = []
            if isinstance(option_roles, list):
                for optionRole in option_roles:
                    rids.append(optionRole)
            else:
                self.dvls_logger.error("Invalid role(s) specified", verbose_override)
            options['CustomRoles'] = rids
        new_user = init_model('generated', 'UserEntity')
        new_user.UserSecurity.CustomSecurityEntity = init_model('generated', 'CustomSecurity')
        new_user.UserAccount.TwoFactorInfo = init_model('generated', 'TwoFactorInfo')
        new_user = fill_data(new_user, options)
        new_user.UserSecurity.ID = user_info['key']
        if 'AuthenticationType' not in options:
            new_user.UserSecurity.AuthenticationType = user_info['userSecurity']['authenticationType']
        return new_user

    @staticmethod
    def object_to_flatten_dict(object_to_flattent, options):
        entry_mod = DVLSConnection._flatten_entry(object_to_flattent)
        entry_mod = DVLSConnection._toUpperFirstLetter(entry_mod)
        return dict(ChainMap({}, options, entry_mod))

    @staticmethod
    def extract_verbose_override_option(options):
        verbose_override = None
        if 'verbose_override' in options and isinstance(options['verbose_override'], bool):
            verbose_override = options['verbose_override']
        return verbose_override
