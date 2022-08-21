import requests
import time
import hmac
import hashlib
import json

secret_key = ''
public_key = ''

url = "https://api.kuna.io/v3/auth/kuna_codes/redeem"
api_path = "/v3/auth/kuna_codes/redeem"

nonce = str(int(time.time()*1000))
payload = {"code": "nnnnn-nnnnn-nnnnn-nnnnn-nnnnn-nnnnn-nnnnn-nnnnn-nnnnn-UAH-KCode"} # code example
body = json.dumps(payload)
msg = api_path+nonce+body
kun_signature = hmac.new(secret_key.encode('ascii'), msg.encode('ascii'), hashlib.sha384).hexdigest()

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'kun-nonce': nonce,
    'kun-apikey': public_key,
    'kun-signature': kun_signature
}

def activate(url, payload, headers, body):
    try:
        response = requests.request("PUT", url, json=payload, headers=headers, data=body) # general request for activation of code
        redeem_state = str(response).split(' ')[1][1:4] # status code
        if redeem_state in ('400', '404', '500'): # if the status is one of
            return "code is incorrect"
        elif redeem_state == '200':
            return "code activated successfully"
    except Exception as e:
        print("error: ", e)