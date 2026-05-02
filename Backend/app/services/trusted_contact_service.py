from fastapi import HTTPException
from sqlalchemy.orm import session
from app.models.trsuted_contact import TtedContacts
from app.schemas.trusted_contact import TrustedContactCreate,TrustedContactUpdate



def validate_phone_number(phone_number: str):
    if not phone_number.isdigit():
        raise HTTPException(status_code=400,detail = "Phone number must contain only digits")
    