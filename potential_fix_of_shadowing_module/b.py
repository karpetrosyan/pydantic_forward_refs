from pydantic import BaseModel


class B(BaseModel):
    not_a: int
