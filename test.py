from cgitb import small
import requests
import json

from dotenv import load_dotenv
import os
load_dotenv()
apikey = os.getenv('APIKEY')

all = []

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': apikey, 
}
dummypayload1 = {
    "collection": "flicmembers",
    "database": "test",
    "dataSource": "Cluster0",
    "filter": {},
}

def find():
    all = requests.post(url = 'https://data.mongodb-api.com/app/data-mkxfx/endpoint/data/v1/action/find', data = json.dumps(dummypayload1), headers=headers)

    return all.json()['documents']

x = find()

import time
def update():
    print('run')
    for i in x:
        newpayload = {
            "collection": "flicmembers",
            "database": "test",
            "dataSource": "Cluster0",
            "filter": {"name" : str(i['name'])},
            "update" : {"$set": {"name": str(i['name']).lower()}}
        }

        pay = {
            "collection": "flicmembers",
            "database": "test",
            "dataSource": "Cluster0",
            "filter": {"name" : str(i['name'])}
        }
        requests.post(url = 'https://data.mongodb-api.com/app/data-mkxfx/endpoint/data/v1/action/updateOne', data = newpayload, headers=headers)
        print(requests.post(url = 'https://data.mongodb-api.com/app/data-mkxfx/endpoint/data/v1/action/findOne', data = pay, headers=headers))
        time.sleep(2)
        
update()