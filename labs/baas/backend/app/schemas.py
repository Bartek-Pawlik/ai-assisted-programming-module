"""Pydantic models for the notes API.

This file defines the basic data models for our notes application.
We'll start simple and add validation rules later in the lab.
"""

from __future__ import annotations

from pydantic import BaseModel


class NoteBase(BaseModel):
    """Base model with the core fields for a note."""
    title: str
    content: str


class NoteCreate(NoteBase):
    """Model for creating a new note (same as NoteBase for now)."""
    pass


class Note(NoteBase):
    """Complete note model with database fields."""
    id: str
    created_at: str
