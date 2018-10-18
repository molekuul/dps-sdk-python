import copy
import xml.etree.ElementTree as ET
from dvlssdk.InitHelpers import *
from dvlssdk.EntryType import *

class ApiTesting:

    class ActionTypes(Enum):
        GET = 'GET'
        CREATE = 'CREATE'
        MODIFY = 'MODIFY'
        DELETE = 'DELETE'

    def __init__(self, DVLS, logger, num_users):
        self.DVLS = DVLS
        self.logger = logger
        self.total_users = num_users
        self.total_tests = 0
        self.tests_succeeded = 0
        self.action_types = ApiTesting.ActionTypes

    def login_test(self, user, password):
        result = self.DVLS.login(user, password)
        self.test("Login:", self.ActionTypes.GET, user, result)

    def logout_test(self, user):
        result = self.DVLS.logout(user)
        self.test("Logout:", self.ActionTypes.GET, user,result)

    def create_role_test(self, name, **options):
        server_data = None
        response = self.DVLS.create_role(name, **options)
        if response.success:
            server_data = self.DVLS.get_role_by_name(name)
        options["Name"] = name
        self._test_with_validation("Create role", self.ActionTypes.CREATE, response, options, server_data)

    def modify_role_by_name_test(self, name, **options):
        server_existing_result = self.DVLS.get_role_by_name(name)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_entry = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_entry, options)
            response = self.DVLS.modify_role_by_name(name, **options)
            if response.success:
                modified_entry = response.data
        return self._test_with_validation("Modify role by name", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def modify_role_by_id_test(self, role_id, **options):
        server_existing_result = self.DVLS.get_role_by_id(role_id)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_entry = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_entry, options)
            response = self.DVLS.modify_role_by_id(role_id, **options)
            if response.success:
                modified_entry = response.data
        return self._test_with_validation("Modify role by id", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def delete_role_by_id_test(self, role_id):
        test_result = False
        response = self.DVLS.delete_role_by_id(role_id)
        if response.success:
            get_result = self.DVLS.get_role_by_id(role_id)
            if not get_result.success:
                test_result = True
        self.process_test_result(test_result, "Delete role by id", role_id)

    def create_security_group_test(self, name, **options):
        server_data = None
        response = self.DVLS.create_security_group(name, **options)
        if response.success:
            if not response.data is None:
                security_group = response.data
                security_group_id = security_group.get('id')
                result = self.DVLS.get_security_group_by_id(security_group_id)
                if result.success:
                    server_data = result.data
        options["Name"] = name
        self._test_with_validation("Create security group", self.ActionTypes.CREATE, response, options, server_data)

    def modify_security_group_test(self, name, **options):
        server_existing_result = self.DVLS.get_security_group_by_name(name)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_entry = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_entry, options)
            response = self.DVLS.modify_security_group_by_name(name, **options)
            if response.success:
                modified_entry = response.data
        return self._test_with_validation("Modify security group", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def get_security_group_tree_test(self, expected_sec_groups):
        server_sec_groups = None
        response = self.DVLS.get_security_group_tree()
        if response.success:
            server_sec_groups = len(response.data)
        self._test_with_validation("Get security group tree", self.ActionTypes.GET, response, server_sec_groups, expected_sec_groups)

    def create_user_test(self, name, user_type,  password, **options):
        response = self.DVLS.create_user(user_type, name, password, **options)
        options["Name"] = name
        options["Password"] = password
        created_user = response.data
        if self._test_with_validation("Create user", self.ActionTypes.CREATE, response, options, created_user):
            self.total_users += 1

    def modify_user_by_name_test(self, name, **options):
        server_existing_result = self.DVLS.get_user_by_name(name)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_entry = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_entry, options)
            response = self.DVLS.modify_user_by_name(name, **options)
            if response.success:
                modified_entry = response.data
        return self._test_with_validation("Modify user by name", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def modify_user_by_id_test(self, user_id, **options):
        server_existing_result = self.DVLS.get_user_by_id(user_id)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_entry = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_entry, options)
            response = self.DVLS.modify_user_by_id(user_id, **final_dict)
            if response.success:
                modified_entry = response.data
        return self._test_with_validation("Modify user by id", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def delete_user_by_name_test(self, name):
        test_result = False
        response = self.DVLS.delete_user_by_name(name)
        if response.success:
            get_result = self.DVLS.get_user_by_name(name)
            if not get_result.success:
                test_result = True
        self.process_test_result(test_result, "Delete user by name", name)

    def delete_user_by_id_test(self, user_id):
        test_result = False
        response = self.DVLS.delete_user_by_id(user_id)
        if response.success:
            get_result = self.DVLS.get_user_by_id(user_id)
            if not get_result.success:
                test_result = True
        self.process_test_result(test_result, "Delete user by id", user_id)

    def create_connection_test(self, name, connection_type, **options):
        created_connection = None
        response = self.DVLS.create_connection(connection_type, name, **options)
        if response.success:
            options["Name"] = name
            if isinstance(connection_type, str) and connection_type in self.STANDARD_ENTRY_TYPES:
                type_id = ConnectionType.value_from_name(connection_type)
            else:
                type_id = connection_type.value
            options["ConnectionType"] = type_id
            created_connection = response.data
        self._test_with_validation("Create connection", self.ActionTypes.CREATE, response, options, created_connection)

    def delete_connection_by_id_test(self, connection_id):
        test_result = False
        response = self.DVLS.delete_connection_by_id(connection_id)
        if response.success:
            get_result = self.DVLS.get_connection_by_id(connection_id)
            if (get_result.success and get_result.data == {}) or not get_result.success:
                test_result = True
        self.process_test_result(test_result, "Delete connection", connection_id)

    def create_credential_test(self, credential_type, name, **options):
        created_credential = None
        response = self.DVLS.create_credential_entry(credential_type, name, **options)
        options["Name"] = name
        if isinstance(credential_type, str) and credential_type in CREDENTIAL_ENTRY_TYPES:
            type_id = CredentialResolverConnectionType.value_from_name(credential_type)
        else:
            type_id = credential_type.value
        options["ConnectionType"] = type_id
        if response.success:
            created_credential = response.data
        self._test_with_validation("Create credential entry", self.ActionTypes.CREATE, response, options, created_credential)

    def modify_credential_test(self, entry_type, name, **options):
        server_existing_result = self.DVLS.get_credential_entries_by_name(name)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_cred = server_existing_result.data[0]
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_cred, options)
            response = self.DVLS.modify_credential_entry(entry_type, server_existing_cred.get('id'), **options)
            if response.success:
                modified_entry = response.data
        self._test_with_validation("Modify credential entry", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def delete_credential_by_id_test(self, credential_id):
        test_result = False
        response = self.DVLS.delete_credential_entry_by_id(credential_id)
        if response.success:
            get_result = self.DVLS.get_credential_entry_by_id(credential_id)
            if (get_result.success and get_result.data == {}) or not get_result.success:
                test_result = True
        self.process_test_result(test_result, "Delete credential entry", credential_id)

    def modify_connection_test(self, entry_type, connection_id, **options):
        server_existing_result = self.DVLS.get_connection_by_id(connection_id)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_conn = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_conn, options)
            response = self.DVLS.modify_connection_by_id(entry_type, connection_id, **options)
            if response.success:
                modified_entry = response.data
        self._test_with_validation("Modify connection", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def modify_features_test(self, **options):
        server_existing_result = self.DVLS.get_features()
        original_entry = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_features = server_existing_result.data
            original_entry = self.DVLS.object_to_flatten_dict(server_existing_features, options)
            response = self.DVLS.modify_features(**options)
            if response.success:
                modified_entry_result = self.DVLS.get_features()
                features_configuration_entity = init_model('generated', 'FeaturesConfigurationEntity')
                modified_entry = fill_data(features_configuration_entity, modified_entry_result.data)
        self._test_with_validation("Modify features", self.ActionTypes.MODIFY, response, original_entry, modified_entry)

    def create_password_template_test(self, mode, name, **options):
        server_template = None
        response = self.DVLS.create_password_template(mode, name, **options)
        if response.success:
            pw_id = response.data
            server_template_result = self.DVLS.get_password_template_by_id(pw_id)
            if server_template_result.success:
                server_template = server_template_result.data
        options["Name"] = name
        options["Mode"] = mode
        self._test_with_validation("Create password template", self.ActionTypes.CREATE, response, options, server_template)

    def modify_password_template_test(self, template_id, **options):
        server_existing_result = self.DVLS.get_password_template_by_id(template_id)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_template = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_template, options)
            response = self.DVLS.modify_password_template(template_id, **options)
            if response.success:
                modified_entry_result = self.DVLS.get_password_template_by_id(template_id)
                if modified_entry_result.success:
                    modified_entry = modified_entry_result.data
        self._test_with_validation("Modify password template", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def delete_password_template_by_id_test(self, template_id):
        test_result = False
        response = self.DVLS.delete_password_template_by_id(template_id)
        if response.success:
            get_result = self.DVLS.get_password_template_by_id(template_id)
            if get_result.success:
                if get_result.data == {}:
                    test_result = True
        self.process_test_result(test_result, "Delete password template", template_id)

    def get_user_id_test(self, username):
        server_user_id = None
        expected_user_id = None
        response = self.DVLS.get_user_id(username)
        if response.success:
            server_user_id = response.data
            server_user_response = self.DVLS.get_user_by_name(username)
            if server_user_response.success:
                user = server_user_response.data
                expected_user_id = user.get("key")
        self._test_with_validation("Get user id", self.ActionTypes.GET, response, server_user_id, expected_user_id)

    def get_users_test(self):
        server_users = None
        expected_users = self.total_users
        response = self.DVLS.get_users()
        if response.success:
            server_users = len(response.data)
        self._test_with_validation("Get users", self.ActionTypes.GET, response, server_users, expected_users)

    def get_sensitive_data_test(self, connection_id, expected_sensitive_data):
        sensitive_data = None
        sensitive_data_result = self.DVLS.get_connection_sensitive_data(connection_id)
        if sensitive_data_result.success:
            sensitive_data = sensitive_data_result.data
        else:
            self.logger.error("Could not get senstive data for " + str(connection_id))
        self._test_with_validation("Get sensitive data", self.ActionTypes.GET, sensitive_data_result, sensitive_data, expected_sensitive_data)

    def get_password_test(self, connection_id, expected_password):
        password = None
        password_result = self.DVLS.get_connection_password(connection_id)
        if password_result.success:
            password = password_result.data
        self._test_with_validation("Get password", self.ActionTypes.GET, password_result, password, expected_password)

    def create_repository_test(self, repo_name, **options):
        creation_result = False
        repo_result = self.DVLS.create_repository(repo_name, **options)
        if repo_result.success:
            get_result = self.DVLS.get_repository_id(repo_name)
            if get_result.success:
                if not get_result.data is None:
                    creation_result = True
        self.process_test_result(creation_result, "Create repository", repo_name)

    def delete_repository_test(self, repo_name):
        delete_result = False
        repo_result = self.DVLS.delete_repository_by_name(repo_name)
        if repo_result.success:
            get_result = self.DVLS.get_repository_id(repo_name)
            if not get_result.success:
                if get_result.data is None:
                    delete_result = True
        self.process_test_result(delete_result, "Delete repository", repo_name)

    def change_repository_test(self, repo_name, expected_entries):
        test_result = False
        change_result = self.DVLS.change_repository(repo_name)
        if change_result.success:
            entries_result = self.DVLS.get_repository_entries_list()
            if entries_result.success:
                server_entries = len(entries_result.data)
                if expected_entries == server_entries:
                    test_result = True
        self.process_test_result(test_result, "Change repository", repo_name)

    def create_private_vault_entry_test(self, name, entry_type, **options):
        creation_result = False
        entry_result = self.DVLS.create_private_vault_entry(entry_type, name, **options)
        if entry_result.success:
            get_result = self.DVLS.get_private_vault_entries_by_name(name)
            if get_result.success:
                if len(get_result.data) == 1:
                    creation_result = True
        self.process_test_result(creation_result, "Create private vault entry", name)

    def modify_private_vault_entry_test(self, entry_type, entry_id, **options):
        server_existing_result = self.DVLS.get_private_vault_entry_by_id(entry_id)
        final_dict = None
        modified_entry = None
        response = None
        if server_existing_result.success:
            server_existing_conn = server_existing_result.data
            final_dict = self.DVLS.object_to_flatten_dict(server_existing_conn, options)
            response = self.DVLS.modify_private_vault_entry_by_id(entry_type, entry_id, **options)
            if response.success:
                modified_entry = response.data
        self._test_with_validation("Modify private vault entry", self.ActionTypes.MODIFY, response, final_dict, modified_entry)

    def delete_private_vault_entry_test(self, entry_id):
        delete_result = False
        repo_result = self.DVLS.delete_private_vault_entry_by_id(entry_id)
        if repo_result.success:
            get_result = self.DVLS.get_private_vault_entry_by_id(entry_id)
            if not get_result.success:
                if get_result.data is None:
                    delete_result = True
        self.process_test_result(delete_result, "Delete private vault entry", entry_id)

    def get_private_vault_list_test(self, expected_entries):
        server_entries = None
        response = self.DVLS.get_private_vault_entries_list()
        if response.success:
            server_entries = len(response.data)
        self._test_with_validation("Get private vault entries list", self.ActionTypes.GET, response, server_entries, expected_entries)

    @staticmethod
    def flatten_entry(entry_dict):
        acc = {}
        for key, value in entry_dict.items():
            if isinstance(value, dict):
                res = ApiTesting.flatten_entry(value)
                acc = dict(acc, **res)
            elif isinstance(value, primitiveTypes):
                acc[key] = value
            elif not isinstance(value, types.FunctionType) and not isinstance(value, Enum) and not key.startswith('_'):
                res = ApiTesting.flatten_entry(vars(value))
                acc = dict(acc, **res)
        return copy.deepcopy(acc)

    @staticmethod
    def transformValues(entry_dict):
        if 'group' in entry_dict and 'connectionType' in entry_dict:
            group = entry_dict.get('group')
            connectionType = entry_dict.get('connectionType')
            if connectionType == ConnectionType.Group.value:
                index = group.rfind('\\')
                if not index == -1:
                    entry_dict['group'] = group[0:index]

    @staticmethod
    def toUpperFirstLetter(entry_dict):
        acc = {}
        upper = lambda s: s[:1].upper() + s[1:] if s else ''
        for key, value in entry_dict.items():
            key = upper(key)
            acc[key] = value
        entry_dict = acc

    @staticmethod
    def extract_custom_security(user):
        if 'CustomSecurity' in user:
            root = ET.fromstring(user.get('CustomSecurity'))
            for child in root:
                if child.tag == 'CustomRoles':
                    role_ids = []
                    for roles in child:
                        role_ids.append(roles.text)
                    user[child.tag] = role_ids
                else:
                    if child.text == 'true':
                        user[child.tag] = True
                    elif child.text == 'false':
                        user[child.tag] = False

    def _validate_object( self, data, server_object):
        if not isinstance(server_object, dict):
            server_object = vars(server_object)
        flattenedData = ApiTesting.flatten_entry(data)
        flattenedObject = ApiTesting.flatten_entry(server_object)
        ApiTesting.transformValues(flattenedObject)
        ApiTesting.toUpperFirstLetter(flattenedObject)
        ApiTesting.extract_custom_security(flattenedObject)
        for key, value in flattenedData.items():
            if key in flattenedObject:
                if not (key == 'Password' and value == ''):
                    if not value == flattenedObject.get(key):
                        self.logger.error("Object validation failed for key: " + str(key) + " value: " + str(value) +
                                          ", object value: " + str(flattenedObject.get(key)))
                        return False
        return True

    @staticmethod
    def _validate_value(test_value, server_value):
        if not test_value == server_value:
            return False
        return True

    def process_test_result(self, result, action_name, name):
        self.total_tests += 1
        if result:
            self.logger.info('[ SUCCESS ] - ' + str(action_name) + " " + str(name))
            self.tests_succeeded += 1
        else:
            self.logger.info('[  FAIL   ] - ' + str(action_name) + " " + str(name))
            pass
        return result

    def _test_with_validation(self, action_name, action_type, response, original_data, expected_data):
        name = None
        result = False
        if not (response is None or original_data is None or expected_data is None):
            result = response.success
            if action_type not in self.ActionTypes:
                self.logger.error('Parameter action_type is not a valid ApiTesting.ActionTypes value.')
                result = False
            # Only validate if API operation was a success
            if response.success:
                if isinstance(original_data, dict):
                    if 'Name' in original_data:
                        name = original_data.get('Name')
                    if not self._validate_object(original_data, expected_data):
                        result = False
                else:
                    name = expected_data
                    if not ApiTesting._validate_value(original_data, expected_data):
                        result = False
        return self.process_test_result(result, action_name, name)


    def test(self, action_name, action_type, name, result):
        if action_type not in self.ActionTypes:
            self.logger.error('Parameter action_type is not a valid ApiTesting.ActionTypes value.')
            result = False

        if action_type is self.ActionTypes.CREATE or action_type is self.ActionTypes.MODIFY:
            self.logger.info('           #' + action_name + " " + name)

        return self.process_test_result(result, action_name, name)