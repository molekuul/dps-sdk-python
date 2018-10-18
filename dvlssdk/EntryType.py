from .generated.enums.ConnectionType import *
from .generated.enums.ContactConnectionType import *
from .generated.enums.DataEntryConnectionType import *
from .generated.enums.CredentialResolverConnectionType import *

STANDARD_ENTRY_TYPES = [c.name for c in ConnectionType]
CONTACT_ENTRY_TYPES = [c.name for c in ContactConnectionType]
DATA_ENTRY_TYPES = [c.name for c in DataEntryConnectionType]
CREDENTIAL_ENTRY_TYPES = [c.name for c in CredentialResolverConnectionType]