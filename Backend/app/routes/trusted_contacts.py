from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.trusted_contact import (
    TrustedContactCreate,
    TrustedContactUpdate,
    TrustedContactResponse
)
from app.services import trusted_contact_service


router = APIRouter(
    prefix="/trusted-contacts",
    tags=["Trusted Contacts"]
)


# temporary current user
# later replace this with JWT auth current_user
def get_current_user_id():
    return 1


@router.post("/", response_model=TrustedContactResponse)
def create_contact(
    data: TrustedContactCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.add_contact(db, user_id, data)


@router.get("/", response_model=list[TrustedContactResponse])
def read_contacts(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.get_contacts(db, user_id)


@router.get("/sos", response_model=list[TrustedContactResponse])
def read_sos_contacts(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.get_sos_contacts(db, user_id)


@router.put("/{contact_id}", response_model=TrustedContactResponse)
def edit_contact(
    contact_id: int,
    data: TrustedContactUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.update_contact(db, user_id, contact_id, data)


@router.delete("/{contact_id}")
def remove_contact(
    contact_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.delete_contact(db, user_id, contact_id)