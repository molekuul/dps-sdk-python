from dvlssdk import DVLSConnection

DVLS_URI = 'http://127.0.0.1/dvls'
DVLS = DVLSConnection(DVLS_URI, errorLevelLog='INFO')
print(DVLS.__version__)

print(DVLS.version)