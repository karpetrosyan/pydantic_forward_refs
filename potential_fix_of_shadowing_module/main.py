from models import a
from models import b as real_b
import b


print(a.A.__pydantic_complete__)  # False
print(a.A.__annotations__)
# a.A.model_rebuild(_types_namespace={"b": real_b})
a.A.model_rebuild(_types_namespace={"B": real_b.B})  # or like this
print(
    a.A.model_json_schema()["$defs"]["B"]["properties"]
)  # {'not_a': {'title': 'Not A', 'type': 'integer'}}
