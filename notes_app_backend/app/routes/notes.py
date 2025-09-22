"""
Notes routes providing RESTful CRUD endpoints.
"""
from http import HTTPStatus
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.schemas.note import NoteSchema, NoteCreateSchema, NoteUpdateSchema
from app.services.notes_service import NotesService
from app.repositories.notes_repository import NotesRepository

# Instantiate repository and service (simple DI for this small app)
_notes_repository = NotesRepository()
_notes_service = NotesService(_notes_repository)

blp = Blueprint(
    "Notes",
    "notes",
    url_prefix="/api/notes",
    description="CRUD endpoints for managing notes",
)


@blp.route("/")
class NotesListResource(MethodView):
    """
    Provides listing and creation of notes.
    """

    @blp.response(HTTPStatus.OK, NoteSchema(many=True))
    @blp.doc(summary="List all notes", description="Retrieve an array of all notes ordered by id.")
    def get(self):
        """
        Get all notes.

        Returns:
            200 OK: A list of notes.
        """
        notes = _notes_service.list_notes()
        return notes

    @blp.arguments(NoteCreateSchema)
    @blp.response(HTTPStatus.CREATED, NoteSchema)
    @blp.doc(summary="Create a new note", description="Create and return the newly created note.")
    def post(self, payload):
        """
        Create a note.

        Parameters:
            payload: JSON body matching NoteCreateSchema

        Returns:
            201 Created: The newly created note.
        """
        note = _notes_service.create_note(title=payload["title"], content=payload["content"])
        return note, HTTPStatus.CREATED


@blp.route("/<int:note_id>")
class NoteResource(MethodView):
    """
    Provides retrieval, update, and deletion of a single note by id.
    """

    @blp.response(HTTPStatus.OK, NoteSchema)
    @blp.doc(summary="Get a note by ID", description="Fetch a single note by its unique identifier.")
    def get(self, note_id: int):
        """
        Get a single note.

        Path:
            note_id (int): Note identifier

        Returns:
            200 OK: The requested note.
            404 Not Found: If the note does not exist.
        """
        note = _notes_service.get_note(note_id)
        if not note:
            abort(HTTPStatus.NOT_FOUND, message="Note not found")
        return note

    @blp.arguments(NoteUpdateSchema, as_kwargs=False)
    @blp.response(HTTPStatus.OK, NoteSchema)
    @blp.doc(summary="Update a note", description="Update title and/or content for the note by ID.")
    def patch(self, payload, note_id: int):
        """
        Partially update a note.

        Path:
            note_id (int): Note identifier
        Body:
            payload: JSON with optional title/content

        Returns:
            200 OK: The updated note.
            404 Not Found: If the note does not exist.
        """
        note = _notes_service.update_note(note_id, title=payload.get("title"), content=payload.get("content"))
        if not note:
            abort(HTTPStatus.NOT_FOUND, message="Note not found")
        return note

    @blp.response(HTTPStatus.NO_CONTENT)
    @blp.doc(summary="Delete a note", description="Delete a note by its unique identifier.")
    def delete(self, note_id: int):
        """
        Delete a note.

        Path:
            note_id (int): Note identifier

        Returns:
            204 No Content: If deletion was successful.
            404 Not Found: If the note does not exist.
        """
        deleted = _notes_service.delete_note(note_id)
        if not deleted:
            abort(HTTPStatus.NOT_FOUND, message="Note not found")
        return "", HTTPStatus.NO_CONTENT
