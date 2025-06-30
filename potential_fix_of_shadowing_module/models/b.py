from pydantic import BaseModel


class B(BaseModel):
    a: "a.A"


from . import a
