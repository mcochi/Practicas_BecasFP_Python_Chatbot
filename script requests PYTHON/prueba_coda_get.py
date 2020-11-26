import requests

headers = {'Authorization': 'Bearer 3bba5e87-358c-498c-9e19-01ee158fddd0'}
uri = 'https://coda.io/apis/v1/docs'

res = requests.get(uri, headers=headers).json()

print(f'First doc is: {res["items"][0]["name"]}')
