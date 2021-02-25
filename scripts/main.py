import json
import requests
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/login"
# REFRESH_ENDPOINTS= AUTH_ENDPOINTS+'refresh/'
# ENDPOINTS='http://127.0.0.1:8000/api/auth/login'
headers={
    "Content-Type":"application/json"
}
data={
    'username':'andyb243',
    'password':'1234',

}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token=r.json()
print(token)