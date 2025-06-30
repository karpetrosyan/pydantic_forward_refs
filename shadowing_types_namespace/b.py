from pydantic import BaseModel


class B(BaseModel):
    a: "A"
    c: "C"


from a import A
from c import C
