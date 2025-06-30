from pydantic import BaseModel


class C(BaseModel):
    b: "B"
    a: "A"


from b import B
from inner.a import A
