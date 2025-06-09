from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.backend.db import Base

class Post(Base):
    __tablename__='blogposts'
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String(255), nullable=False)
    main_text=Column(Text, nullable=False)
    date=Column(DateTime, default=datetime.utcnow)