import jsonschema
from jsonschema import validate
import jsonschema.exceptions
import requests

user_schema={
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "username": {"type": "string"},
        "password": {"type": "string"},
        "created_at":{"type": "string"}
    },
    "required": ["username", "password"],
    "additionalProperties": False
}
