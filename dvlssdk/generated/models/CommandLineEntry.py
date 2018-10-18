from dvlssdk.generated.enums.CmdParamDataType import *
from dvlssdk.generated.enums.CommandLineCaptureOutputMode import *
from dvlssdk.generated.enums.CommandLineExecutionMode import *
from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.enums.RunAsCredentialSource import *
from dvlssdk.generated.models.SensitiveItem import *


class CommandLineEntry:
    def __init__(self):
        self.CaptureOutputFilePath = ''
        self.CaptureOutputMode = CommandLineCaptureOutputMode(0)
        self.CommandLine = ''
        self.CommandLineWaitForApplicationToExit = False
        self.CredentialConnectionId = ''
        self.CredentialConnectionID = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.CredentialSource = RunAsCredentialSource(0)
        self.Domain = ''
        self.EmbeddedWaitTime = 250
        self.ExecutionMode = CommandLineExecutionMode(0)
        self.Host = ''
        self.NetOnly = False
        self.Parameter1DataType = CmdParamDataType(0)
        self.Parameter1DefaultValue = ''
        self.Parameter1Label = 'Parameter #1'
        self.Parameter2DataType = CmdParamDataType(0)
        self.Parameter2DefaultValue = ''
        self.Parameter2Label = 'Parameter #2'
        self.Parameter3DataType = CmdParamDataType(0)
        self.Parameter3DefaultValue = ''
        self.Parameter3Label = 'Parameter #3'
        self.Parameter4DataType = CmdParamDataType(0)
        self.Parameter4DefaultValue = ''
        self.Parameter4Label = 'Parameter #4'
        self.Parameter5DataType = CmdParamDataType(0)
        self.Parameter5DefaultValue = ''
        self.Parameter5Label = 'Parameter #5'
        self.PasswordItem = SensitiveItem()
        self.PrivateVaultSearchString = ''
        self.ProcessName = ''
        self.Run64BitsMode = False
        self.RunAsAdministrator = False
        self.RunAsDomain = ''
        self.RunAsPasswordItem = SensitiveItem()
        self.RunAsPromptForCredentials = False
        self.RunAsUsername = ''
        self.UseDefaultWorkingDirectory = True
        self.Username = ''
        self.UseShellExecute = True
        self.WorkingDirectory = ''

