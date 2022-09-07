from re import A
from fastapi                import APIRouter, Body
from fastapi.encoders       import jsonable_encoder

from server.controllers.response import(
    ErrorResponseModel,
    ResponseModel,
)

from server.controllers.roles.main import(
    add_role,
    all_roles,
    delete_role,
    id_role,
    update_role
)

from server.models.roles import(
    RolSchema,
    UpdateRoleModel
)

router = APIRouter()

@router.get("/", response_description="Roles")
async def get_roles():
    roles = await all_roles()
    if roles:
        return ResponseModel(roles, "Roles exitosamente")
    return ResponseModel(roles, "Sin Roles")

@router.post("/create", response_description="Creación del rol")
async def create_role(role: RolSchema = Body(...)):
    role      = jsonable_encoder(role)
    new_role  = await add_role(role)
    if new_role:
        return ResponseModel(new_role, "Se ha creado el rol exitosamente")
    return ErrorResponseModel("Ocurrió un problema.", 404, "Intente más tarde" )

@router.get("/{id}", response_description="role by id")
async def get_role_data(id):
    role = await id_role(id)
    if role:
        return ResponseModel(role, "Role Exitoso")
    return ErrorResponseModel("Ocurrió un problema.", 404, "No existe el rol.")

@router.put("/{id}")
async def update_role_data(id: str, req: UpdateRoleModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_role = await update_role(id, req)
    if updated_role:
        return ResponseModel(
            "role with ID: {} ha sido actualizado correctamento, ID:".format(id),
            "actualizado",
        )
    return ErrorResponseModel("Ocurrió un problema.", 404, "Ocurrió un problema al actualizar el rol")

@router.delete("/{id}", response_description="Role eliminado de la base de datos")
async def delete_role_data(id: str):
    deleted_role = await delete_role(id)
    if deleted_role:
        return ResponseModel(
            "Role con el ID: {} eliminado".format(id), "Role eliminado exitosamente"
        )
    return ErrorResponseModel( "Ocurrió un problema.", 404, "Role con el id {0} no existe".format(id))