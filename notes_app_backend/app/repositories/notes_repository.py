"""
In-memory repository for managing Note entities.

This is a simple repository to fulfill the CRUD behavior without an external DB.
Swap this implementation with a persistent storage when needed.
"""
from threading import RLock
from typing import Dict, List, Optional
from datetime import datetime

from app.models.note import Note


class NotesRepository:
    """
    Repository providing CRUD operations on Note entities.
    Thread-safe for single-process usage with a re-entrant lock.
    """

    def __init__(self) -> None:
        self._notes: Dict[int, Note] = {}
        self._next_id: int = 1
        self._lock = RLock()

    def list_notes(self) -> List[Note]:
        """Return all notes sorted by id ascending."""
        with self._lock:
            return sorted(self._notes.values(), key=lambda n: n.id)

    def get_note(self, note_id: int) -> Optional[Note]:
        """Return a note by id or None if not found."""
        with self._lock:
            return self._notes.get(note_id)

    def create_note(self, title: str, content: str) -> Note:
        """Create and store a new note."""
        with self._lock:
            note = Note(id=self._next_id, title=title, content=content)
            self._notes[self._next_id] = note
            self._next_id += 1
            return note

    def update_note(self, note_id: int, title: Optional[str] = None, content: Optional[str] = None) -> Optional[Note]:
        """Update fields on a note if it exists, returning updated note or None."""
        with self._lock:
            note = self._notes.get(note_id)
            if not note:
                return None
            if title is not None:
                note.title = title
            if content is not None:
                note.content = content
            note.updated_at = datetime.utcnow()
            self._notes[note_id] = note
            return note

    def delete_note(self, note_id: int) -> bool:
        """Delete a note by id. Returns True if deleted, False if not found."""
        with self._lock:
            if note_id in self._notes:
                del self._notes[note_id]
                return True
            return False
