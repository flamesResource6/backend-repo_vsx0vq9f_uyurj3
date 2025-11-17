"""
Database Schemas for Portfolio App

Each Pydantic model represents a MongoDB collection. The collection name is the
lowercase of the class name (e.g., ContactMessage -> "contactmessage").
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class ContactMessage(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=2000)
    source: Optional[str] = Field(default="portfolio", description="Where the message was sent from")

class Project(BaseModel):
    title: str
    description: Optional[str] = None
    tags: List[str] = []
    live: Optional[str] = None
    repo: Optional[str] = None
    image: Optional[str] = None
