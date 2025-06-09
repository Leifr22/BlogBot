from pydantic import BaseModel
from datetime import datetime

class CreatePost(BaseModel):
    title: str
    main_text: str
class ReadPost(CreatePost):
    id: int
    date: datetime

    class Config:
        orm_mode=True

