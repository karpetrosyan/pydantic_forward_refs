from pydantic import BaseModel


class B(BaseModel):
    a: "A"


from a import A
