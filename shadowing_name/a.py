from pydantic import BaseModel


class A(BaseModel):
    b: "B"


from b import B
