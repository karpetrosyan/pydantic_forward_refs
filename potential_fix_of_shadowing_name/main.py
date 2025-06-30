from pydantic import BaseModel
from b import B
from a import A as TrueA


class A(BaseModel):
    not_b: int


print(B.__pydantic_complete__)  # False
B.model_rebuild(_types_namespace={"A": TrueA})
print(
    B.model_json_schema()["$defs"]["A"]["properties"]
)  # {'not_b': {'title': 'Not B', 'type': 'integer'}}
