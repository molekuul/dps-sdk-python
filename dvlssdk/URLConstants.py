from string import Template


class UrlResolver(object):
    # paths used to communicate to the server's RESTful API
    CONNECTION = Template('$dvls_uri/api/connections/partial/$entry_id')
    DELETE_REPOSITORY = Template('$dvls_uri/api/security/repositories/$id')
    DELETE_REPOSITORY_MOVE_ENTRIES = Template('$dvls_uri/api/security/repositories/$id/$new_id')
    DELETE_ROLE = Template('$dvls_uri/api/security/roleinfo/delete/$id')
    DELETE_SECURITY_GROUP = Template('$dvls_uri/api/security/groupinfo/delete/$id')
    DELETE_USER = Template('$dvls_uri/api/security/userinfo/delete/$id')
    DELETE_PRIVATE_ENTRY = Template('$dvls_uri/api/connections/partial/$id')
    ENTRIES_TREE = Template('$dvls_uri/api/connections/partial/tree')
    GET_PASSWORD = Template('$dvls_uri/api/connections/partial/$id/sensitive-data')
    LOGIN = Template('$dvls_uri/api/login')
    LOGOUT = Template('$dvls_uri/api/logout')
    FEATURES = Template('$dvls_uri/api/configuration/features')
    PASSWORD_TEMPLATE = Template('$dvls_uri/api/password-configuration')
    PRIVATE_VAULT_TREE = Template('$dvls_uri/api/privateconnections/partial')
    REPOSITORIES = Template('$dvls_uri/api/security/current-user-repositories')
    ROLES_TREE = Template('$dvls_uri/api/security/roles')
    SECURITY_GROUP_BY_NAME = Template('$dvls_uri/api/security/groupinfo/name/$name')
    SECURITY_GROUP_BY_ID = Template('$dvls_uri/api/security/groupinfo/$id')
    SECURITY_GROUP_TREE = Template('$dvls_uri/api/security/groupinfos')
    SENSITIVE_DATA = Template('$dvls_uri/api/connections/partial/$id/sensitive-data')
    SAVE_ENTRY = Template('$dvls_uri/api/connections/partial/save')
    SAVE_REPOSITORY = Template('$dvls_uri/api/security/repositories')
    SAVE_ROLE = Template('$dvls_uri/api/security/role/save?csToXml=1')
    SAVE_SECURITY_GROUP = Template('$dvls_uri/api/security/groupinfo/save')
    SAVE_USER = Template('$dvls_uri/api/security/user/save?csToXml=1')
    SERVER_INFO = Template('$dvls_uri/api/server-information')
    SWITCH_REPOSITORY = Template('$dvls_uri/api/security/repositories/change')
    USERS_TREE = Template('$dvls_uri/api/security/users?csFromXml=1')
    GET_USER = Template('$dvls_uri/api/security/user/$userid')

    def __init__(self, dvls_uri):
        self.dvls_uri = dvls_uri

    def connection_byid_url(self, entry_id):
        return self.CONNECTION.substitute(dvls_uri=self.dvls_uri, entry_id=entry_id)

    def delete_repository_url(self, repo_id):
        return self.DELETE_REPOSITORY.substitute(dvls_uri=self.dvls_uri, id=repo_id)

    def delete_repository_move_entries_url(self, delete_id, move_to_id):
        return self.DELETE_REPOSITORY_MOVE_ENTRIES.substitute(dvls_uri=self.dvls_uri, id=delete_id, new_id=move_to_id)

    def delete_role_url(self, role_id):
        return self.DELETE_ROLE.substitute(dvls_uri=self.dvls_uri, id=role_id)

    def delete_security_group_url(self, sec_id):
        return self.DELETE_SECURITY_GROUP.substitute(dvls_uri=self.dvls_uri, id=sec_id)

    def delete_user_url(self, user_id):
        return self.DELETE_USER.substitute(dvls_uri=self.dvls_uri, id=user_id)

    def delete_private_entry_url(self, entry_id):
        return self.DELETE_PRIVATE_ENTRY.substitute(dvls_uri=self.dvls_uri, id=entry_id)

    def entries_tree_url(self):
        return self.ENTRIES_TREE.substitute(dvls_uri=self.dvls_uri)

    def get_password_url(self, user_id):
        return self.GET_PASSWORD.substitute(dvls_uri=self.dvls_uri, id=user_id)

    def get_sensitive_data(self, connection_id):
        return self.SENSITIVE_DATA.substitute(dvls_uri=self.dvls_uri, id=connection_id)

    def login_url(self):
        return self.LOGIN.substitute(dvls_uri=self.dvls_uri)

    def logout_url(self):
        return self.LOGOUT.substitute(dvls_uri=self.dvls_uri)

    def features_url(self):
        return self.FEATURES.substitute(dvls_uri=self.dvls_uri)

    def password_template_url(self):
        return self.PASSWORD_TEMPLATE.substitute(dvls_uri=self.dvls_uri)

    def private_vault_tree_url(self):
        return self.PRIVATE_VAULT_TREE.substitute(dvls_uri=self.dvls_uri)

    def user_repositories_url(self):
        return self.REPOSITORIES.substitute(dvls_uri=self.dvls_uri)

    def roles_url(self):
        return self.ROLES_TREE.substitute(dvls_uri=self.dvls_uri)

    def security_group_by_id_url(self, sc_id):
        return self.SECURITY_GROUP_BY_ID.substitute(dvls_uri=self.dvls_uri, id=sc_id)

    def security_group_by_name_url(self, name):
        return self.SECURITY_GROUP_BY_NAME.substitute(dvls_uri=self.dvls_uri, name=name)

    def security_groups_url(self):
        return self.SECURITY_GROUP_TREE.substitute(dvls_uri=self.dvls_uri)

    def save_entry_url(self):
        return self.SAVE_ENTRY.substitute(dvls_uri=self.dvls_uri)

    def save_repository_url(self):
        return self.SAVE_REPOSITORY.substitute(dvls_uri=self.dvls_uri)

    def save_role_url(self):
        return self.SAVE_ROLE.substitute(dvls_uri=self.dvls_uri)

    def save_security_group_url(self):
        return self.SAVE_SECURITY_GROUP.substitute(dvls_uri=self.dvls_uri)

    def save_user_url(self):
        return self.SAVE_USER.substitute(dvls_uri=self.dvls_uri)

    def server_info_url(self):
        return self.SERVER_INFO.substitute(dvls_uri=self.dvls_uri)

    def change_repository_url(self):
        return self.SWITCH_REPOSITORY.substitute(dvls_uri=self.dvls_uri)

    def users_url(self):
        return self.USERS_TREE.substitute(dvls_uri=self.dvls_uri)

    def get_user_url(self, user_id):
        return self.GET_USER.substitute(dvls_uri=self.dvls_uri, userid=user_id)