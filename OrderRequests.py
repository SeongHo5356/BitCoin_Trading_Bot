import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = os.environ['gEPXNBKV6hB83L8xbW2xMQI8WTT3IFK7Yd6etyDL']
secret_key = os.environ['AtxlkHqEuQWTU8ERC2sthRCoRxJiHaeveQXajcDc']
server_url = os.environ['https://api.upbit.com/v1/orders']

query = {
    'market': 'KRW-BTC',
    'side': 'bid',
    'volume': '0.0015',
    'price': '100.0',
    'ord_type': 'price',
}
query_string = urlencode(query).encode()

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, secret_key).decode('utf-8')
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.post(server_url + "/v1/orders", params=query, headers=headers)