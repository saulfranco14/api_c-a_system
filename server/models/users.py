from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UsersSchema( BaseModel ):
    name_user           : str               = Field(...)
    first_name_user     : str               = Field(...)
    last_name_user      : str               = Field(...)
    email_user          : EmailStr          = Field(...)
    active_user         : Optional[bool]
    passsword_user      : Optional[str]
    id_rol              : int

    class Config:
        schema_extra = {
            "example" : {
                "name_user"         : "Saul Mauricio",
                "first_name_user"   : "Franco",
                "last_name_user"    : "Rentería",
                "email_user"        : "fars_9301@hotmail.com",
                "passsword_user"    : "******",
                "id_rol"            : 1,
                "active_user"       : True,
            }
        }

class UpdateUserModel(BaseModel):
    name_user           : Optional[str]
    first_name_user     : Optional[str]
    last_name_user      : Optional[str]
    email_user          : Optional[str]
    passsword_user      : Optional[str]
    id_rol              : Optional[str]
    active_user         : Optional[str]

    class Config:
        schema_extra = {
            "example" : {
                "name_user"         : "Saul Mauricio",
                "first_name_user"   : "Franco",
                "last_name_user"    : "Rentería",
                "email_user"        : "fars_9301@hotmail.com",
                "passsword_user"    : "*****",
                "id_rol"            : 1,
                "active_user"       : False,
            }
        }