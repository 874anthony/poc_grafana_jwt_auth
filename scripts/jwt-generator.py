import jwt
import time
import webbrowser

payload = {
    "user": "foobar",
    "sub": "foobar@example.com",
    "iat": int(time.time())
}

token = jwt.encode(payload, 'S@mepl@ce123!', algorithm='HS256')

print('Token: ', token)

base_url = 'http://localhost'

url_with_token = f'{base_url}?auth_token={token}'
print('URL WITH TOKEN: ', url_with_token)

# webbrowser.open_new_tab(url_with_token)