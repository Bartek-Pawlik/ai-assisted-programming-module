"""FastAPI entrypoint for the notes backend.

This is a simple note-taking API that demonstrates:
- REST API design with FastAPI
- Firebase Firestore integration
- AI-assisted development with GitHub Copilot
"""

# FastAPI framework and utilities
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

# Local application imports
from . import firestore  # Database operations
from .schemas import Note, NoteCreate  # Data models (Pydantic)

# Initialize the FastAPI application with metadata
app = FastAPI(title="Firebase Notes API", version="0.1.0")

# Configure CORS (Cross-Origin Resource Sharing)
# This allows the React frontend (running on a different port) to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development only)
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


# Root endpoint: Redirects users to the API documentation
@app.get("/", include_in_schema=False)
def root():
    """Redirect to docs."""
    return RedirectResponse(url="/docs")


# Health check endpoint: Used to verify the API is running
@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


# List Notes: GET /notes
# Returns a list of all notes stored in the database
@app.get("/notes", response_model=list[Note], tags=["notes"])
def list_notes() -> list[Note]:
    """Get all notes from Firestore."""
    return firestore.list_notes()


# Create Note: POST /notes
# Accepts a JSON payload (title, content), saves it, and returns the created note
@app.post(
    "/notes",
    response_model=Note,
    status_code=201,  # 201 Created is the standard status for successful creation
    tags=["notes"],
)
def create_note(payload: NoteCreate) -> Note:
    """Create a new note in Firestore."""
    return firestore.create_note(payload)


# Delete Note: DELETE /notes/{note_id}
# Removes a specific note by its ID
@app.delete("/notes/{note_id}", status_code=204, tags=["notes"])
def delete_note(note_id: str) -> None:
    """Delete a note from Firestore."""
    firestore.delete_note(note_id)
