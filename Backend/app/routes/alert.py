# import os
# from dotenv import load_dotenv

# from twilio.rest import Client


# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session

# from app.utils.database import get_db
# from app.schemas.sos_request import SOSTriggerRequest
# from app.controller.trusted_contact_service import get_sos_contacts


# load_dotenv()


# router = APIRouter(prefix="/alert", tags=["fetch_SOS_contact"])

# account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# twilio_number = os.getenv("TWILIO_NUMBER")

# if not all([account_sid, auth_token, twilio_number]):
#     raise RuntimeError("Missing Twilio configuration.")

# client = Client(account_sid,auth_token)


# @router.post("/sos_trigger")
# def trigger_sos_from_ml(
#     data : SOSTriggerRequest,
#     db: Session = Depends(get_db)
# ):
#     contacts = get_sos_contacts(db, data.userId)

#     if not contacts:
#         raise HTTPException(
#             status_code=404,
#             detail=f"No SOS contacts found for user_id {data.userId}"
#         )
    
#     if not data.location:
#         raise HTTPException(status_code=400, detail="Location data is required to send an SOS alert")

#     message_text = f"""
# 🚨 EMERGENCY ALERT 🚨
# User may be in danger!

# Location:
# https://maps.google.com/?q={data.location.lat},{data.location.lng}

# Threat: {data.threat_type}
# Confidence: {data.confidence}
# """


#     send_to = []

#     for con in contacts:
#         full_number = f"{con.country_code}{con.phoneNo}"

#         try:
#             client.messages.create(
#                 body=message_text,
#                 from_=twilio_number,
#                 to=full_number
#             )

#             send_to.append(full_number)
#             print(f"SMS sent to {full_number}")
#         except Exception as e:
#             print(f"failed for {full_number}: {e}")
#     return{
#         "message": "SOS alert sent successfully",
#         "sent_to": send_to
#     }