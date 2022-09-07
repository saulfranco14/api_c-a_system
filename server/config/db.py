import  motor.motor_asyncio
import  os
from    decouple import  config

Mongo_Details   = config("MONGODB_URL")
client          = motor.motor_asyncio.AsyncIOMotorClient(Mongo_Details)
database        = client.c_a_api

def Database(table):
    data_collection = database.get_collection(table)
    return data_collection