from pydantic import BaseModel, EmailStr


class Item(BaseModel):
    title: str
    surname: str
    address: str
    telefon: str
    email: EmailStr
    url: str
    google_map: str
    open_street_map: str
