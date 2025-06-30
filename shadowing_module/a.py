from pydantic import BaseModel


class A(BaseModel):
    b: "shadowing_module.models.b.B"


import shadowing_module.models.b as b
