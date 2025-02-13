import hashlib
import os

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def check_integrity(file_path, original_hash):
    """Compare the current hash with the original to detect changes."""
    current_hash = calculate_hash(file_path)
    if current_hash == original_hash:
        print(f"[SAFE] {file_path} has not been modified.")
    else:
        print(f"[WARNING] {file_path} has been modified!")

# Example usage
file_to_monitor = "test.txt"  # Replace with actual file path
original_hash = calculate_hash(file_to_monitor)
print(f"Original Hash: {original_hash}")

# Simulate a change in the file
check_integrity(file_to_monitor, original_hash)



