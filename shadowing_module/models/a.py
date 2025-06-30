from pydantic import BaseModel


class A(BaseModel):
    b: "b.B"


from . import b
