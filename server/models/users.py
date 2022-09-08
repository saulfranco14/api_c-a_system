from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UsersSchema( BaseModel ):
    name_user           : str               = Field(...)
    first_name_user     : str               = Field(...)
    last_name_user      : str               = Field(...)
    phone_user          : str               = Field(...)
    email_user          : EmailStr          = Field(...)
    id_rol              : str               = Field(...)
    password_user       : Optional[str]

    class Config:
        schema_extra = {
            "example" : {
                "name_user"         : "Saul Mauricio",
                "first_name_user"   : "Franco",
                "last_name_user"    : "Rentería",
                "phone_user"        : '5585999485',
                "email_user"        : "fars_9301@hotmail.com",
                "password_user"     : "chelsea",
                "id_rol"            : "users",
            }
        }

class UpdateUserModel(BaseModel):
    name_user           : Optional[str]
    first_name_user     : Optional[str]
    last_name_user      : Optional[str]
    email_user          : Optional[str]
    password_user       : Optional[str]
    id_rol              : Optional[str]
    phone_user          : Optional[str]

    class Config:
        schema_extra = {
            "example" : {
                "name_user"         : "Saul Mauricio",
                "first_name_user"   : "Franco",
                "last_name_user"    : "Rentería",
                "phone_user"        : '5585999485',
                "email_user"        : "fars_9301@hotmail.com",
                "password_user"     : "chelsea",
                "id_rol"            : "admin",
            }
        }