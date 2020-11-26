import requests

#headers = {'Authorization': 'Bearer 3bba5e87-358c-498c-9e19-01ee158fddd0'}
#uri = 'https://coda.io/apis/v1/docs'
uri = 'https://merqueo.com/api/3.1/stores/63/department/97/shelves?zoneId=40'

#params = {
#  'isOwner': True,
 # 'query': 'New',
#}
res = requests.get(uri).json()

print(f'First doc is: {res["data"][0]["id"]}')
# => First doc is: New Document
