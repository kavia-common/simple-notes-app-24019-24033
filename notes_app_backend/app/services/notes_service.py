"""
Service layer for Notes business logic.
"""
from typing import List, Optional

from app.models.note import Note
from app.repositories.notes_repository import NotesRepository


class NotesService:
    """
    Provides use-case level operations for Notes using the repository.
    """

    def __init__(self, repository: NotesRepository) -> None:
        self.repository = repository

    # PUBLIC_INTERFACE
    def list_notes(self) -> List[Note]:
        """Return all notes."""
        return self.repository.list_notes()

    # PUBLIC_INTERFACE
    def get_note(self, note_id: int) -> Optional[Note]:
        """Return a single note by id, or None if not found."""
        return self.repository.get_note(note_id)

    # PUBLIC_INTERFACE
    def create_note(self, title: str, content: str) -> Note:
        """Create a new note."""
        return self.repository.create_note(title=title, content=content)

    # PUBLIC_INTERFACE
    def update_note(self, note_id: int, title: Optional[str] = None, content: Optional[str] = None) -> Optional[Note]:
        """Update an existing note and return it, or None if not found."""
        return self.repository.update_note(note_id=note_id, title=title, content=content)

    # PUBLIC_INTERFACE
    def delete_note(self, note_id: int) -> bool:
        """Delete a note by id. Returns True if deleted."""
        return self.repository.delete_note(note_id)
