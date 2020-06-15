AWS = 'https://aws.amazon.com/SAML/Attributes/'


MAP = {
    'identifier': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
    'fro': {
        AWS + 'Role': 'RoleEntitlement',
        AWS + 'RoleSessionName': 'RoleSessionName',
        AWS + 'SessionDuration': 'SessionDuration',
        AWS + 'TransitiveTagKeys': 'TransitiveTagKeys',
        'userPrincipalName': 'userPrincipalName',
    },
    'to': {
        'RoleEntitlement': AWS + 'Role',
        'RoleSessionName': AWS + 'RoleSessionName',
        'SessionDuration': AWS + 'SessionDuration',
        'TransitiveTagKeys': AWS + 'TransitiveTagKeys',     
        'userPrincipalName': 'userPrincipalName',
    }
}

