from models import a
import b

print(a.A.__pydantic_complete__)  # False
a.A.model_rebuild()
print(
    a.A.model_json_schema()["$defs"]["B"]["properties"]
)  # {'not_a': {'title': 'Not A', 'type': 'integer'}}
