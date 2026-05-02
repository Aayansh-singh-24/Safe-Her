from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class TrustedContacts(Base):
    __tablename__ = "trusted_contact"
    id = Column(Integer,primary_key=True,index=True)
    userId = Column(Integer,ForeignKey("user.id"),nullable=False)
    name = Column(String,nullable=False)
    phoneNo = Column(String,default="+91")
    isSOS = Column(Boolean,default=False)
    owner = relationship("User" , back_populates="TrustedContact")