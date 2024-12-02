from bson import ObjectId
from pydantic import GetCoreSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from typing import Any

class PyObjectId(ObjectId):
    """
    Custom ObjectId untuk digunakan dengan Pydantic.
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """
        Definisikan schema Pydantic-core untuk PyObjectId.
        """
        return core_schema.no_info_plain_validator_function(cls.validate)

    @classmethod
    def validate(cls, value: Any) -> "PyObjectId":
        """
        Validasi input dan konversi ke PyObjectId.
        """
        if not ObjectId.is_valid(value):
            raise ValueError(f"Invalid ObjectId: {value}")
        return cls(value)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, schema: JsonSchemaValue, handler: Any
    ) -> JsonSchemaValue:
        """
        Modifikasi schema JSON agar ObjectId direpresentasikan sebagai string.
        """
        schema.update({"type": "string", "format": "objectid"})
        return schema

