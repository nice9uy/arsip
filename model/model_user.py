from bson import ObjectId
from pydantic import BaseModel, Field
from .model_common import PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    password: str
    name: str

    class Config:
        populate_by_name = True  # Memungkinkan menggunakan alias saat inisialisasi
        json_encoders = {
            ObjectId: str  # Konversi ObjectId menjadi string saat serialisasi JSON
        }