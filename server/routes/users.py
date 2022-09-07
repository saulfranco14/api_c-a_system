from re import A
from fastapi                import APIRouter, Body
from fastapi.encoders       import jsonable_encoder

from server.controllers.response import(
    ErrorResponseModel,
    ResponseModel,
)

from server.controllers.users.main import(
    add_user,
    all_users,
    delete_user,
    id_user,
    update_user
)

from server.models.users import(
    UsersSchema,
    UpdateUserModel
)

router = APIRouter()

@router.get("/", response_description="Usuarios")
async def get_users():
    users = await all_users()
    if users:
        return ResponseModel(users, "Usuarios exitosamente")
    return ResponseModel(users, "Sin Usuarios")

@router.post("/create", response_description="Creación del usuario")
async def create_user(user: UsersSchema = Body(...)):
    user      = jsonable_encoder(user)
    new_user  = await add_user(user)
    if new_user:
        return ResponseModel(new_user, "Se ha creado el usuario exitosamente")
    return ErrorResponseModel("Ocurrió un problema.", 404, "Intente más tarde" )

@router.get("/{id}", response_description="User by id")
async def get_user_data(id):
    user = await id_user(id)
    if user:
        return ResponseModel(user, "Usuario Exitoso")
    return ErrorResponseModel("Ocurrió un problema.", 404, "No existe el usuario.")

@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "Usuario con ID: {} ha sido actualizado correctamento.".format(id),
            "actualizado",
        )
    return ErrorResponseModel("Ocurrió un problema.", 404, "Ocurrió un problema al actualizar el usuario")

@router.delete("/{id}", response_description="Usuario eliminado de la base de datos")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "Usuario con el ID: {} eliminado".format(id), "Usuario eliminado exitosamente"
        )
    return ErrorResponseModel( "Ocurrió un problema.", 404, "Usuario con el id {0} no existe".format(id))