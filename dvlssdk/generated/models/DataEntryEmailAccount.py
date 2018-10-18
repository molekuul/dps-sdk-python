from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.EmailAuthenticationType import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *


class DataEntryEmailAccount:
    def __init__(self):
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Email = ''
        self.IMAPAuthentication = EmailAuthenticationType(0)
        self.IMAPHostName = ''
        self.IMAPPasswordItem = SensitiveItem()
        self.IMAPPort = 143
        self.IMAPSSL = False
        self.IMAPUserName = ''
        self.POPAuthentication = EmailAuthenticationType(0)
        self.POPHostName = ''
        self.POPPasswordItem = SensitiveItem()
        self.POPPort = 110
        self.POPSSL = False
        self.POPUserName = ''
        self.SMIME = False
        self.SMTPAuthentication = EmailAuthenticationType(0)
        self.SMTPHostName = ''
        self.SMTPPasswordItem = SensitiveItem()
        self.SMTPPort = 25
        self.SMTPRequiresAuthentication = False
        self.SMTPSSL = False
        self.SMTPUserName = ''
        self.SMTPUseSamesAsIncoming = False
        self.Url = ''
        self.YourName = ''

