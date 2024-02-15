import base64

# Your secret value
secret = "S@mepl@ce123!"

# Convert to Base64 URL Encoded string
encoded_secret = base64.urlsafe_b64encode(secret.encode()).decode().rstrip('=')

print(encoded_secret)
