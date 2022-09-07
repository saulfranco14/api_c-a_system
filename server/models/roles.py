from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class RolSchema( BaseModel ):
    name_rol        : str           = Field(...)
    url_rol         : str           = Field(...)
    description_rol : Optional[str]
    menu_rol        : Optional[list]

    class Config:
        schema_extra = {
            "example" : {
                "name_rol" : "admin",
                "description_rol" : "Rol for administrative in the enterprise",
                "url_rol" : "admin/dashboard",
                "menu_rol" : ["users", "dashboard", "roles"]
            }
        }

class UpdateRoleModel(BaseModel):
    name_rol        : Optional[str]
    url_rol         : Optional[str]
    description_rol : Optional[str]
    menu_rol        : Optional[list]

    class Config:
        schema_extra = {
            "example" : {
                "name_rol" : "admin",
                "description_rol" : "Rol for administrative in the enterprise",
                "url_rol" : "admin/dashboard",
                "menu_rol" : ["users", "roles"]
            }
        }