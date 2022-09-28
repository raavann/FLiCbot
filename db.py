# import aiohttp
# import json

# from dotenv import load_dotenv
# import os
# load_dotenv()
# apikey = os.getenv('APIKEY')

# headers = {
#     'Content-Type': 'application/json',
#     'Access-Control-Request-Headers': '*',
#     'api-key': apikey, 
# }
# dummypayload = {
#     "collection": "flicmembers",
#     "database": "test",
#     "dataSource": "Cluster0"
# }

# # async function,  give it filter and it will return the result in dictionary
# async def find(filt : dict) -> dict:
#     newpayload = dummypayload
#     newpayload['filter'] = filt
#     payload = json.dumps(newpayload)

#     async with aiohttp.ClientSession() as session:
#         async with session.post(url = 'https://data.mongodb-api.com/app/data-mkxfx/endpoint/data/v1/action/findOne', data = payload, headers=headers) as response:
#             html = await response.json(content_type=None)

#             if(type(html) != dict):
#                 return html
#             return(html['document'])

# async def update(filt:dict, update : dict ) ->None:
#     newpayload = dummypayload
#     newpayload['update'] = update
#     newpayload['filter'] = filt
#     payload = json.dumps(newpayload)

#     async with aiohttp.ClientSession() as session:
#         async with session.post(url = 'https://data.mongodb-api.com/app/data-mkxfx/endpoint/data/v1/action/updateOne', data = payload, headers=headers) as response:
#             return


# motor
from dotenv import load_dotenv
import os
load_dotenv()
uri = os.getenv('uri')

import motor.motor_asyncio
db = motor.motor_asyncio.AsyncIOMotorClient(uri)

async def find(filt: dict) -> dict:
    document = await db.test.flicmembers.find_one(filt)
    return document

async def update(filt:dict, update : dict ) ->None:
    result = await db.test.flicmembers.replace_one(filt, update)
    return
