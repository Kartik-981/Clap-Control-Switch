from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_file(data, key):
    """Encrypt data using AES-256."""
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + encrypted_data).decode()

def decrypt_file(encrypted_data, key):
    """Decrypt AES-256 encrypted data."""
    raw_data = base64.b64decode(encrypted_data)
    iv = raw_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(raw_data[AES.block_size:]), AES.block_size)
    return decrypted_data.decode()

# Example usage
key = b'16byteslongkey12'  # Must be 16, 24, or 32 bytes
original_text = "Confidential Data"
encrypted = encrypt_file(original_text, key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_file(encrypted, key)
print(f"Decrypted: {decrypted}")

