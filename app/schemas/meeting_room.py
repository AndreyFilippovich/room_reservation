from typing import Optional

from pydantic import BaseModel


class MeetingRoomCreate(BaseModel):
    name: str
    description: Optional[str]
