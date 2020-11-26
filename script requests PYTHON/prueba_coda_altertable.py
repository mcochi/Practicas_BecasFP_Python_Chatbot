import requests

headers = {'Authorization': 'Bearer 3bba5e87-358c-498c-9e19-01ee158fddd0'}
uri = f'https://coda.io/apis/v1/docs/luIET5FNUy/tables'
res = requests.get(uri, headers=headers).json()
longitud = len(res['items'])

for i in range(0,longitud):
    print('The name of the table is ' + str(res['items'][i]['id']))


#print(f'The name of the first table is {res["items"][0]["name"]}')
# => The name of the first table is To-do List
