from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""


def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """

    pass


def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """

    pass