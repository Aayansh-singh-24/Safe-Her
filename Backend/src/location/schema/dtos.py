from pydantic import BaseModel
from typing import Optional

class locationAlertSchema(BaseModel):
    latitude : float
    longitude : float
    message:Optional[str]=None