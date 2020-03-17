from dvlssdk.CSV_FileOps import DVLS_CSV_File
from dvlssdk import DVLSConnection

# Test reading a csv from a zip with a password
zip_file = "./../tests/EntryList.zip"
zip_pwd = " "
RDM_CSV_export = DVLS_CSV_File(zip_file, zip_pwd)
RDM_CSV_content = RDM_CSV_export.get_csv_content()

# Test creating a zip (without password) with a csv containing modified values
for row in RDM_CSV_content:
    if row['ConnectionType'] == 'SSH Tunnel':
        row['CredentialUserName'] = 'UserName_C'
        row['CredentialPassword'] = 'Password_C'
RDM_CSV_export.modify_zipped_csv(RDM_CSV_content)

# Test reading the tree of entries from a DVLS server
DVLS_URI = 'http://127.0.0.1/dvls'
DVLS_server = DVLSConnection(DVLS_URI, errorLevelLog='WARNING')
DVLS_ADMIN_USER = 'mainuser'
DVLS_ADMIN_PW = '123456'

DVLS_server.login(DVLS_ADMIN_USER, DVLS_ADMIN_PW)
repo_id = DVLS_server.get_repository_id("Default")
repo_entries_list = DVLS_server.get_repository_entries_list(repo_id)
prv_vlt_entries_list = DVLS_server.get_private_vault_entries_list()
repo_and_prv_vlt_entries_list = repo_entries_list.data + prv_vlt_entries_list.data
DVLS_server.logout(DVLS_ADMIN_USER)
    
# Test writing the list of DVLS entries to a newly created zipped CSV
DVLS_export_file_name = "./../tests/DVLS_CSV_export_test.zip"
DVLS_new_csv_export = DVLS_CSV_File(DVLS_export_file_name)
DVLS_new_csv_export.create_zipped_csv(repo_and_prv_vlt_entries_list)

# Test modifying the DVLS entries in the newly created zipped CSV
DVLS_modified_csv_file_name = "./../tests/DVLS_modified_CSV_test.zip"
DVLS_modified_csv = DVLS_CSV_File(DVLS_modified_csv_file_name)
DVLS_modified_csv_content = DVLS_new_csv_export.get_csv_content()
for row in DVLS_modified_csv_content:
    if row['keywords'] == "Tag1 Tag2" and row['name'] == "SSH Shell Entry":
        row['keywords'] = "Tag3 Tag4"
DVLS_modified_csv.create_zipped_csv(DVLS_modified_csv_content)

