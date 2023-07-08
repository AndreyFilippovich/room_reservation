from typing import Optional

from pydantic import BaseModel, Field


# Базовый класс схемы, от которого наследуем все остальные.
class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True
