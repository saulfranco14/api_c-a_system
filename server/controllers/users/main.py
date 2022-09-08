from    server.config.db    import Database
from    bson.objectid       import ObjectId
import  bcrypt



# Connect to Mongo
user_collection = Database("users")

def user_helper(user) ->  dict:

    key_user            = list(user.keys())
    active_user         = None
    password_user       = None
    phone_user          = None
    hash                = None

    if not 'active_user' in key_user:
        active_user
    else:
        active_user = user['active_user']

    if not 'password_user' in key_user:
        password_user
    else:
        password_user = user['password_user']
        bytes     = password_user.encode('utf-8')
        salt      = bcrypt.gensalt()
        hash      = bcrypt.hashpw(bytes, salt)

    if not 'phone_user' in key_user:
        phone_user
    else:
        phone_user = user['phone_user']

    return {
        "id_user"                        : str(user["_id"]),
        "name_user"                      : str(user["name_user"]),
        "first_name_user"                : str(user["first_name_user"]),
        "last_name_user"                 : str(user["last_name_user"]),
        "email_user"                     : str(user["email_user"]),
        "phone_user"                     : phone_user,
        "id_rol"                         : str(user["id_rol"]),
        "password_user"                  : hash,
        "active_user"                    : active_user
    }

async def all_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

async def add_user(user_data: dict) -> dict:

    user      = await user_collection.insert_one(user_data)
    new_user  = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def id_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one( {"_id": ObjectId(id)}, {"$set": data} )
        if updated_user:
            return True
        return False

async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
