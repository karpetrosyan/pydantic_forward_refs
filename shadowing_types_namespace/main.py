from pydantic import BaseModel
from b import B
from a import A as TrueA


class A(BaseModel):
    not_b: int


from c import C

print(C.__annotations__)
print(B.__pydantic_complete__)  # False
B.model_rebuild(_types_namespace={"A": TrueA})
print(B.model_json_schema()["$defs"]["B"]["properties"])  # as expected, real A
print(
    B.model_json_schema()["$defs"]["C"]["properties"]
)  # the same A that in B, though we expected another A

# this is because _types_namespace sometimes should be more specific, to avoid shadowing
