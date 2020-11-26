import requests

headers = {'Authorization': 'Bearer 3bba5e87-358c-498c-9e19-01ee158fddd0'}
uri = 'https://coda.io/apis/v1/docs/luIET5FNUy/tables/grid-gQ8Jgon0FY/rows'
res = requests.get(uri, headers=headers).json()
print(f'The name is: {res["items"][0]["values"]["c-8-8bbB0V_-"]}')
nombre = res["items"][0]["values"]["c-8-8bbB0V_-"]
print(f'The last name is: {res["items"][0]["values"]["c-BQp_yVqvFP"]}')
apellido = res["items"][0]["values"]["c-BQp_yVqvFP"]


yonombre = "adrian"
nombredespuesdeproc = nombre + yonombre
print(nombredespuesdeproc)

yoapellido = "moral"
apellidodespuesdeproc = apellido + yoapellido
print(apellidodespuesdeproc)

 



payload = {
  'rows': [
    {
      'cells': [
        {'column': 'c-8-8bbB0V_-', 'value': nombredespuesdeproc},
        {'column': 'c-BQp_yVqvFP', 'value': apellidodespuesdeproc},
        {'column': 'c-uIq1Yrs1td', 'value': "3" },
      ],
    },
  ],
}
req = requests.post(uri, headers=headers, json=payload)
req.raise_for_status() 
res = req.json()
print(f'Inserted 1 row')






#uri = 'https://coda.io/apis/v1/docs/luIET5FNUy/tables/grid-gQ8Jgon0FY/rows/i-bIuLqB147a/'
#payload = {
#  'row': {
 #   'cells': [
  #      {'column': 'c-8-8bbB0V_-', 'value': nombredespuesdeproc },
   #     {'column': 'c-BQp_yVqvFP', 'value': apellidodespuesdeproc }
    #],
  #},
#}

#req = requests.put(uri, headers=headers, json=payload)
#req.raise_for_status() # Throw if there was an error.
#res = req.json()

#print(f'Inserted 1 row')
# => Inserted 1 row
