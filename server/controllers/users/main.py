from    server.config.db    import Database
from    bson.objectid       import ObjectId


# Connect to Mongo
user_collection = Database("c_a_api")

def user_helper(user) ->  dict:

    key_user            = list(user.keys())
    active_user         = None
    status_civil_user   = None

    if not 'active_user' in key_user:
        active_user
    else:
        active_user = user['active_user']

    if not 'status_civil_user' in key_user:
        status_civil_user
    else:
        status_civil_user = user['status_civil_user']

    return {
        "id_user"                        : str(user["_id"]),
        "name_user"                      : str(user["name_user"]),
        "first_name_user"                : str(user["first_name_user"]),
        "last_name_user"                 : str(user["last_name_user"]),
        "email_user"                     : str(user["email_user"]),
        "id_rol"                         : int(user["id_rol"]),
        "status_civil_user"              : status_civil_user,
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
