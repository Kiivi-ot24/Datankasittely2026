from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""
key = Fernet.generate_key()
f = Fernet(key)



def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """
    encrypted_names = []
    for name in names:
        encrypted_name = f.encrypt(name.encode("utf-8"))
        encrypted_names.append(encrypted_name)

    return encrypted_names


def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """
    decrypted_names = []
    for encrypted_name in encrypted:
        decrypted_name = f.decrypt(encrypted_name).decode("utf-8")
        decrypted_names.append(decrypted_name)
    return decrypted_names