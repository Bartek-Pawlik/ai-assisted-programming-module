"""Firestore helper functions for the notes backend.

TODO for students:
- Use GitHub Copilot to help implement these functions
- Ask Copilot: "Complete the list_notes function to retrieve all documents from the 'notes' collection"
- Ask Copilot: "Complete the create_note function to add a new note with a timestamp"
"""

from __future__ import annotations

from datetime import datetime

from firebase_admin import credentials, firestore, initialize_app

from .schemas import Note, NoteCreate

_FIREBASE_APP_INITIALISED = False


def get_firestore_client() -> firestore.Client:
    """Return a Firestore client, initialising the admin SDK if needed."""
    global _FIREBASE_APP_INITIALISED
    if not _FIREBASE_APP_INITIALISED:
        initialize_app(credentials.ApplicationDefault())
        _FIREBASE_APP_INITIALISED = True
    return firestore.client()


def list_notes() -> list[Note]:
    """Fetch all note documents from the notes collection.
    
    TODO: Use Copilot to complete this function.
    Hint: Get the 'notes' collection, stream documents, convert to Note objects.
    """
    # TODO: Implement this function
    return []


def create_note(payload: NoteCreate) -> Note:
    """Create a note document and return the persisted model.
    
    TODO: Use Copilot to complete this function.
    Hint: Add a 'created_at' timestamp, save to Firestore, return Note with ID.
    """
    # TODO: Implement this function
    # This is a placeholder to make the type checker happy
    return Note(id="placeholder", title="placeholder", content="placeholder", created_at="now")


def delete_note(note_id: str) -> None:
    """Delete a note document from Firestore.
    
    TODO: Use Copilot to complete this function.
    Hint: Get the document reference and call delete().
    """
    # TODO: Implement this function
    pass
