from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.schemas.trusted_contact import (
    TrustedContactCreateSchema,
    TrustedContactUpdate,
    TrustedContactResponse
)
from app.controller import trusted_contact_service


router = APIRouter(
    prefix="/trusted-contacts",
    tags=["Trusted Contacts"]
)


# temporary current user
# later replace this with JWT auth current_user
def get_current_user_id():
    return 1


@router.post("/create_contact", response_model=TrustedContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(
    data: TrustedContactCreateSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.add_contact(db, user_id, data)


@router.get("/read_contacts", response_model=list[TrustedContactResponse],status_code=status.HTTP_200_OK)
def read_contacts(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.get_contacts(db, user_id)


# @router.get("/sos", response_model=list[TrustedContactResponse])
# def read_sos_contacts(
#     db: Session = Depends(get_db),
#     user_id: int = Depends(get_current_user_id)
# ):
#     return trusted_contact_service.get_sos_contacts(db, user_id)


@router.put("/edit_contact/{contact_id}", response_model=TrustedContactResponse, status_code=status.HTTP_200_OK)
def edit_contact(
    contact_id: int,
    data: TrustedContactUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.update_contact(db, user_id, contact_id, data)


@router.delete("/remove_contact/{contact_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_contact(
    contact_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return trusted_contact_service.delete_contact(db, user_id, contact_id)