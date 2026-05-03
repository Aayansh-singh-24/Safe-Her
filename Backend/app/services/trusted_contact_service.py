from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.trsuted_contact import TrustedContacts
from app.schemas.trusted_contact import TrustedContactCreate, TrustedContactUpdate


def validate_phone_number(phone_number: str):
    if not phone_number.isdigit():
        raise HTTPException(
            status_code=400,
            detail="Phone number must contain only digits"
        )

    if len(phone_number) != 10:
        raise HTTPException(
            status_code=400,
            detail="Phone number must be 10 digits"
        )


def add_contact(db: Session, user_id: int, data: TrustedContactCreate):
    validate_phone_number(data.phone_number)

    existing_contact = db.query(TrustedContacts).filter(
        TrustedContacts.userId == user_id,
        TrustedContacts.phoneNo == data.phone_number
    ).first()

    if existing_contact:
        raise HTTPException(
            status_code=400,
            detail="Contact already exists"
        )

    contact = TrustedContacts(
        userId=user_id,
        name=data.name,
        country_code=data.country_code,
        phoneNo=data.phone_number,
        isSOS=data.is_sos_contact
    )

    db.add(contact)
    db.commit()
    db.refresh(contact)

    return contact


def get_contacts(db: Session, user_id: int):
    return db.query(TrustedContacts).filter(
        TrustedContacts.userId == user_id
    ).all()


def get_sos_contacts(db: Session, user_id: int):
    return db.query(TrustedContacts).filter(
        TrustedContacts.userId == user_id,
        TrustedContacts.isSOS.is_(True)
    ).all()


def update_contact(db: Session, user_id: int, contact_id: int, data: TrustedContactUpdate):
    contact = db.query(TrustedContacts).filter(
        TrustedContacts.id == contact_id,
        TrustedContacts.userId == user_id
    ).first()

    if not contact:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )

    if data.name is not None:
        contact.name = data.name

    if data.country_code is not None:
        contact.country_code = data.country_code

    if data.phone_number is not None:
        validate_phone_number(data.phone_number)

        existing_contact = db.query(TrustedContacts).filter(
            TrustedContacts.userId == user_id,
            TrustedContacts.phoneNo == data.phone_number,
            TrustedContacts.id != contact_id
        ).first()

        if existing_contact:
            raise HTTPException(
                status_code=400,
                detail="Contact number already exists"
            )

        contact.phoneNo = data.phone_number

    if data.is_sos_contact is not None:
        contact.isSOS = data.is_sos_contact

    db.commit()
    db.refresh(contact)

    return contact


def delete_contact(db: Session, user_id: int, contact_id: int):
    contact = db.query(TrustedContacts).filter(
        TrustedContacts.id == contact_id,
        TrustedContacts.userId == user_id
    ).first()

    if not contact:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )

    db.delete(contact)
    db.commit()

    return {
        "message": "Contact deleted successfully"
    }