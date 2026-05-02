from pydantic import BaseModel,Field

class TrustedContactCreate(BaseModel):
    name: str = Field(..., min_length=2, max_lenth=50)
    country_code = "+91"
    phone_number :str = Field(..., min_length=7,max_length=15)
    is_sos_contact : bool = False

class TrustedContactUpdate(BaseModel):
    name : str | None = None
    country_code : str | None = None
    phone_number : str | None = None
    is_sos_contact: bool | None = None

class TrustesContactResponse(BaseModel):
    id : int
    name : str
    country_code : str
    phone_number : str
    isSOS : str
