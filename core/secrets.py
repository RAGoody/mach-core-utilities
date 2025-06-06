def getSecret(secretName):
    """
    Retrieve secret from secretName
    :param secretName: Name of the secret to retrieve
    """
    thisSecretPath = os.getenv(secretName)
    secretValue = open(thisSecretPath, 'r').read().strip()
    if not secretValue:
        raise ValueError(f"Secret {secretName} not found.")
    return secretValue