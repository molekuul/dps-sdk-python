import json
import requests

from dvlssdk.URLConstants import UrlResolver
from dvlssdk.EncryptionUtils import EncryptionManager
from dvlssdk.InitHelpers import *
from dvlssdk.custom.SDKResult import SDKResult


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        return obj.__dict__


class ApiManager(object):

    def __init__(self, dvls_uri, dvls_logger):
        self.url_resolver = UrlResolver(dvls_uri)
        self.dvls_logger = dvls_logger
        self.DvlsRequestHeaders = {'Content-Type': 'application/json'}
        self.DvlsUserLoggedIn = None
        self.DvlsTokenID = None
        self.EncryptionManager = None
        self.DvlsUri = dvls_uri
        self.server_info = self.get_server_info().data

    def login(self,  username, password, verbose_override=None):
        """Logs in a user to the DVLS server

        :param username: username of the user to log out
        :param password: password of the user
        :param verbose_override: specify verbose_override=False so that nothing is output to the console
        :return: login succeeded or failed - True or False
        """
        result = SDKResult()
        if self.is_logged_on():
            self.dvls_logger.error("[ApiManager.login] - Unable to log in with '" + username +
                                   "': the previous user is still logged in", verbose_override)
        else:
            self.DvlsRequestHeaders = {'Content-Type': 'application/json'}
            self.EncryptionManager = EncryptionManager(self.server_info, password)

            info = {'UserName': username}
            encrypted_info = self.EncryptionManager.get_encrypted_password()
            info['SafePassword'] = encrypted_info['password']
            info['SafeSessionKey'] = encrypted_info['key']
            data_model = init_model('generated', 'LoginData')
            data_model.RDMOLoginParameters = init_model(
                'generated', 'RDMOLoginParameters')
            data_model.TwoFactorInfo = init_model(
                'generated', 'TwoFactorInfo')
            login_data = fill_data(data_model, info)

            web_request = self._do_api_post_json(self.url_resolver.login_url(), login_data)
            result = SDKResult(web_request.json())
            if result.success:
                self.DvlsUserLoggedIn = username
                self.DvlsTokenID = result.data.get('tokenId')
                self.DvlsRequestHeaders['tokenId'] = self.DvlsTokenID
        return SDKResult(result)

    def logout(self, username, verbose_override=None):
        """Logs out a user from the DVLS server

        :param username: username of the user to log out
        :param verbose_override: specify verbose_override=False so that nothing is output to the console
        :return: logout succeeded or failed - True or False
        """
        result = SDKResult
        if self.is_logged_on() and self.DvlsUserLoggedIn == username:
            web_request = self._do_api_get(self.url_resolver.logout_url())
            self.DvlsRequestHeaders = None
            self.DvlsTokenID = None
            result = SDKResult(web_request.json())
        else:
                self.dvls_logger.info("[ApiManager.login] - User '" + username + "' is not logged in", verbose_override)
        return result

    def is_logged_on(self):
        return self.DvlsTokenID is not None

    def get_server_info(self):
        web_request = self._do_api_get(self.url_resolver.server_info_url())
        return SDKResult(web_request.json())

    def get_active_repository_entries(self, verbose_override=None):
        web_request = self._do_api_post_json(self.url_resolver.entries_tree_url(), '')
        return SDKResult(web_request.json())

    def get_users(self, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.users_url())
        return SDKResult(web_request.json())

    def get_user(self, user_id, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.get_user_url(user_id))
        return SDKResult(web_request.json())

    def delete_user(self, user_id, verbose_override=None):
        web_request = self._do_api_delete(self.url_resolver.delete_user_url(user_id))
        return SDKResult(web_request.json())

    def modify_user(self, user_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_user_url(), user_entry)
        return SDKResult(web_request.json())

    def save_user(self, user_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_user_url(), user_entry)
        return SDKResult(web_request.json())

    def get_security_group_by_id(self, sc_id, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.security_group_by_id_url(sc_id))
        return SDKResult(web_request.json())

    def get_security_group_by_name(self, name, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.security_group_by_name_url(name))
        return SDKResult(web_request.json())

    def create_security_group(self, group_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_security_group_url(), group_entry)
        return SDKResult(web_request.json())

    def modify_security_group(self, group_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_security_group_url(), group_entry)
        return SDKResult(web_request.json())

    def delete_security_group_by_id(self, sc_id, verbose_override=None):
        web_request = self._do_api_delete(self.url_resolver.delete_security_group_url(sc_id))
        return SDKResult(web_request.json())

    def get_security_groups_tree(self, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.security_groups_url())
        return SDKResult(web_request.json())

    def create_role(self, role_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_role_url(), role_entry)
        return SDKResult(web_request.json())

    def modify_role(self, role_entry, verbose_override=None):
        return self.create_role(role_entry)

    def delete_role(self, role_id, verbose_override=None):
        web_request = self._do_api_delete(self.url_resolver.delete_role_url(role_id))
        return SDKResult(web_request.json())

    def get_roles(self, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.roles_url())
        return SDKResult(web_request.json())

    def create_password_template(self, template_entry, verbose_override=None):
        web_request = self._do_api_post_json(self.url_resolver.password_template_url(), template_entry)
        return SDKResult(web_request.json())

    def modify_password_template(self, template_entry):
        web_request = self._do_api_put_json(self.url_resolver.password_template_url(), template_entry)
        return SDKResult(web_request.json())

    def delete_password_template(self, pw_template, verbose_override=None):
        web_request = self._do_api_delete(self.url_resolver.password_template_url(), pw_template)
        return SDKResult(web_request.json())

    def get_password_templates(self, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.password_template_url())
        return SDKResult(web_request.json())

    def get_features(self, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.features_url())
        return SDKResult(web_request.json())

    def modify_features(self, features, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.features_url(), features)
        return SDKResult(web_request.json())

    def create_connection_entry(self, connection_entry, verbose_override=None):
        web_request = self._do_api_post_json(self.url_resolver.save_entry_url(), connection_entry)
        return SDKResult(web_request.json())

    def modify_connection_entry(self, connection_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_entry_url(), connection_entry)
        return SDKResult(web_request.json())

    def create_credential_entry(self, credential_entry, verbose_override=None):
        web_request = self._do_api_post_json(self.url_resolver.save_entry_url(), credential_entry)
        return SDKResult(web_request.json())

    def modify_credential_entry(self, credential_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_entry_url(), credential_entry)
        return SDKResult(web_request.json())

    def delete_entry(self, name, entry, verbose_override=None):
        web_request = self._do_api_delete(self.url_resolver.connection_byid_url(entry['id']), entry)
        return SDKResult(web_request.json())

    def get_private_vault_entries(self, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.private_vault_tree_url())
        return SDKResult(web_request.json())

    def delete_private_vault_entry(self, entry_id, entry, verbose_override=None):
        web_request = self._do_api_delete(self.url_resolver.delete_private_entry_url(entry_id), entry)
        return SDKResult(web_request.json())

    def get_connection_by_id(self, connection_id, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.connection_byid_url(connection_id))
        return SDKResult(web_request.json())

    def get_sensitive_data(self, connection_id, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.get_sensitive_data(connection_id))
        result = SDKResult(web_request.json())
        if result.success:
            data = self.EncryptionManager.aes_decrypt(result.data).decode('utf-8')
            result.data = json.loads(data)
        return result

    def get_repositories(self, verbose_override=None):
        web_request = self._do_api_get(self.url_resolver.user_repositories_url())
        return SDKResult(web_request.json())

    def create_repository(self, repository_entry, verbose_override=None):
        web_request = self._do_api_put_json(self.url_resolver.save_repository_url(), repository_entry)
        return SDKResult(web_request.json())

    def delete_repository_by_id(self, repository_id, verbose_override=None):
        web_request = self._do_api_delete(self.url_resolver.delete_repository_url(repository_id))
        return SDKResult(web_request.json())

    def change_active_repository(self, repository_id, verbose_override):
        web_request = self._do_api_put_json(self.url_resolver.change_repository_url(), repository_id)
        return SDKResult(web_request.json())

    def _do_api_get(self, uri):
        return requests.get(uri, headers=self.DvlsRequestHeaders)

    def _do_api_post_json(self, uri, body):
        hdrs = self.DvlsRequestHeaders
        return requests.post(
            uri, headers=hdrs, data=json.dumps(
                body, cls=Encoder))

    def _do_api_put_json(self, uri, body):
        hdrs = self.DvlsRequestHeaders
        return requests.put(
            uri, headers=hdrs, data=json.dumps(
                body, cls=Encoder))

    def _do_api_delete(self, uri, body=None):
        hdrs = self.DvlsRequestHeaders
        if body:
            response = requests.delete(
                uri, headers=hdrs, data=json.dumps(
                    body, cls=Encoder))
        else:
            response = requests.delete(
                uri, headers=hdrs)
        return response

    def _process_error(self, message, result, verbose_override=None):
        if result.errorMessage is not '' and result.errorMessage is not None:
            self.dvls_logger.error(message + ", Error Description: '" + str(result.errorDesc) + "', Error message: '" + str(result.errorMessage)+ "'", verbose_override , 2)
        else:
            self.dvls_logger.error(message + ", Error Description: '" + str(result.errorDesc) + "'", verbose_override, 2)

