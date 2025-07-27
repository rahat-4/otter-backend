import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class APIKeyCrypto:
    def __init__(self, password: str, salt: bytes = None):
        """
        Initialize the crypto handler with a password.

        Args:
            password (str): Master password for encryption/decryption
            salt (bytes): Optional salt. If None, a random salt will be generated
        """
        if salt is None:
            self.salt = os.urandom(16)  # Generate random 16-byte salt
        else:
            self.salt = salt

        # Derive key from password using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.cipher = Fernet(key)

    def encrypt_api_key(self, api_key: str) -> dict:
        """
        Encrypt an API key.

        Args:
            api_key (str): The API key to encrypt

        Returns:
            dict: Contains 'encrypted_key' and 'salt' (both base64 encoded)
        """
        encrypted_key = self.cipher.encrypt(api_key.encode())

        return {
            "encrypted_key": base64.b64encode(encrypted_key).decode(),
            "salt": base64.b64encode(self.salt).decode(),
        }

    def decrypt_api_key(self, encrypted_data: dict) -> str:
        """
        Decrypt an API key.

        Args:
            encrypted_data (dict): Dictionary with 'encrypted_key' and 'salt'

        Returns:
            str: The decrypted API key
        """
        encrypted_key = base64.b64decode(encrypted_data["encrypted_key"])
        decrypted_key = self.cipher.decrypt(encrypted_key)

        return decrypted_key.decode()


# Convenience functions for one-off operations
def encrypt_api_key(api_key: str, password: str) -> dict:
    """
    Encrypt an API key with a password.

    Args:
        api_key (str): The API key to encrypt
        password (str): Master password for encryption

    Returns:
        dict: Contains 'encrypted_key' and 'salt' (both base64 encoded)
    """
    crypto = APIKeyCrypto(password)
    return crypto.encrypt_api_key(api_key)


def decrypt_api_key(encrypted_data: dict, password: str) -> str:
    """
    Decrypt an API key with a password.

    Args:
        encrypted_data (dict): Dictionary with 'encrypted_key' and 'salt'
        password (str): Master password for decryption

    Returns:
        str: The decrypted API key
    """
    salt = base64.b64decode(encrypted_data["salt"])
    crypto = APIKeyCrypto(password, salt)
    return crypto.decrypt_api_key(encrypted_data)


# # Encrypt the API key
# encrypted_data = encrypt_api_key(api_key, master_password)

# # Decrypt the API key
# decrypted_key = decrypt_api_key(encrypted_data, master_password)
