import hashlib

def number_to_short_token(number):
    # Convert number to bytes (assuming it's a string representation)
    number_bytes = str(number).encode('utf-8')
    
    # Hash the bytes using SHA-256 (you can choose other hash algorithms like SHA-1 or MD5)
    hashed = hashlib.sha256(number_bytes).hexdigest()
    
    # Take the first 10 characters of the hashed value
    short_token = hashed[:10]
    
    return short_token

# Example usage
number = 123456
token = number_to_short_token(number)
print(f"Token for {number}: {token}")
