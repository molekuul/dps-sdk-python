from dvlssdk import DVLSConnection
import datetime

from dvlssdk import ConnectionType
from dvlssdk.generated.enums.CommandLineCaptureOutputMode import CommandLineCaptureOutputMode
from dvlssdk.generated.enums.CommandLineExecutionMode import CommandLineExecutionMode

# Constants
# DVLS_URI = 'http://127.0.0.1/dvlsSDK'
DVLS_URI = 'http://127.0.0.1/dvls'
DVLS = DVLSConnection(DVLS_URI, errorLevelLog='INFO')
DVLS_ADMIN_USER = 'mainuser'
DVLS_ADMIN_PW = '123456'

ST_ENTRIES = DVLS.STANDARD_ENTRY_TYPES
CT_ENTRIES = DVLS.CONTACT_ENTRY_TYPES
DT_ENTRIES = DVLS.DATA_ENTRY_TYPES
NO_DISPLAY = False

TIME_CURRENT = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute)
TIME_IN_ONE_HOUR = str(datetime.datetime.now().hour + 1) + ':' + str(datetime.datetime.now().minute)
TOMORROW = str(datetime.datetime.now() + datetime.timedelta(1))

print("---------------------------------------------------------------------------------------------\n")
print("           ######################")
print("           ### Create Entries ###")
print("           ######################")
print(" ")

DVLS.login(DVLS_ADMIN_USER, DVLS_ADMIN_PW)

for i in range(500):
    DVLS.create_connection(
        ConnectionType.CommandLine,
        "Command Line Entry " + str(i),
        CaptureOutputMode=CommandLineCaptureOutputMode.File.value,
        CaptureOutputFilePath='CapOutFilePath',
        CommandLine='CommandLineRun',
        CommandLineWaitForApplicationToExit=True,
        CredentialSource='Custom',
        CredentialConnectionId='CredConId',
        CredentialConnectionID='CredConID',
        Description='Description',
        Domain='Domain',
        EmbeddedWaitTime=500,
        ExecutionMode=CommandLineExecutionMode.Capture.value,
        Expiration=str(datetime.datetime.now()
                       + datetime.timedelta(1)),
        Group='Import',
        Host='Host',
        Keywords='Tag1 Tag2',
        NetOnly=True,
        Parameter1DataType='Secured',
        Parameter1DefaultValue='P1Default',
        Parameter1Label='P1Label',
        Password='Password',
        ProcessName='CommandLineRun',
        Run64BitsMode=True,
        RunAsAdministrator=True,
        RunAsDomain='Domain',
        RunAsPassword='Password',
        RunAsPromptForCredentials=True,
        RunAsUsername='Username')

for i in range(100):
    DVLS.create_connection(
        ConnectionType.CommandLine,
        "Command Line Entry $APPLICATION_NAME$ " + str(i + 500),
        CaptureOutputMode=CommandLineCaptureOutputMode.File.value,
        CaptureOutputFilePath='CapOutFilePath',
        CommandLine='CommandLineRun',
        CommandLineWaitForApplicationToExit=True,
        CredentialSource='Custom',
        CredentialConnectionId='CredConId',
        CredentialConnectionID='CredConID',
        Description='Description',
        Domain='Domain',
        EmbeddedWaitTime=500,
        ExecutionMode=CommandLineExecutionMode.Capture.value,
        Expiration=str(datetime.datetime.now()
                       + datetime.timedelta(1)),
        Group='Import',
        Host='Host',
        Keywords='Tag1 Tag2',
        NetOnly=True,
        Parameter1DataType='Secured',
        Parameter1DefaultValue='P1Default',
        Parameter1Label='P1Label',
        Password='Password',
        ProcessName='CommandLineRun',
        Run64BitsMode=True,
        RunAsAdministrator=True,
        RunAsDomain='Domain',
        RunAsPassword='Password',
        RunAsPromptForCredentials=True,
        RunAsUsername='Username',
        UserName='Username: $HOST$')

for i in range(500):
    DVLS.create_connection(
        ConnectionType.CommandLine,
        "Command Line Entry " + str(i + 600),
        CaptureOutputMode=CommandLineCaptureOutputMode.File.value,
        CaptureOutputFilePath='CapOutFilePath',
        CommandLine='CommandLineRun',
        CommandLineWaitForApplicationToExit=True,
        CredentialSource='Custom',
        CredentialConnectionId='CredConId',
        CredentialConnectionID='CredConID',
        Description='Description',
        Domain='Domain',
        EmbeddedWaitTime=500,
        ExecutionMode=CommandLineExecutionMode.Capture.value,
        Expiration=str(datetime.datetime.now()
                       + datetime.timedelta(1)),
        Group='Import',
        Host='Host',
        Keywords='Tag1 Tag2',
        NetOnly=True,
        Parameter1DataType='Secured',
        Parameter1DefaultValue='P1Default',
        Parameter1Label='P1Label',
        Password='Password',
        ProcessName='CommandLineRun',
        Run64BitsMode=True,
        RunAsAdministrator=True,
        RunAsDomain='Domain',
        RunAsPassword='Password',
        RunAsPromptForCredentials=True,
        RunAsUsername='Username')