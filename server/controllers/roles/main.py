from    server.config.db    import Database
from    bson.objectid       import ObjectId


# Connect to Mongo
role_collection = Database("roles")

def role_helper(role) ->  dict:

    key_role        = list(role.keys())
    description_rol = None
    menu_rol        = None

    if not 'description_rol' in key_role:
        description_rol
    else:
        description_rol = role['description_rol']

    if not 'menu_rol' in key_role:
        menu_rol
    else:
        menu_rol = role['menu_rol']

    return {
        "id_rol"                        : str(role["_id"]),
        "name_rol"                      : str(role["name_rol"]),
        "url_rol"                       : str(role["url_rol"]),
        "description_rol"               : description_rol,
        "menu_rol"                      : menu_rol
    }

async def all_roles():
    roles = []
    async for role in role_collection.find():
        roles.append(role_helper(role))
    return roles

async def add_role(role_data: dict) -> dict:
    role      = await role_collection.insert_one(role_data)
    new_role  = await role_collection.find_one({"_id": role.inserted_id})
    return role_helper(new_role)

async def id_role(id: str) -> dict:
    role = await role_collection.find_one({"_id": ObjectId(id)})
    if role:
        return role_helper(role)


async def update_role(id: str, data: dict):
    if len(data) < 1:
        return False
    role = await role_collection.find_one({"_id": ObjectId(id)})
    if role:
        updated_role = await role_collection.update_one( {"_id": ObjectId(id)}, {"$set": data} )
        if updated_role:
            return True
        return False

async def delete_role(id: str):
    role = await role_collection.find_one({"_id": ObjectId(id)})
    if role:
        await role_collection.delete_one({"_id": ObjectId(id)})
        return True