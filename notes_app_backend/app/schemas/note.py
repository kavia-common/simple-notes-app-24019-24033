"""
Schemas for Notes API validation and serialization.
"""
from marshmallow import Schema, fields, validate


class NoteBaseSchema(Schema):
    """Base fields shared across request/response."""
    title = fields.String(
        required=True,
        description="Title of the note",
        validate=validate.Length(min=1, max=200),
        example="Grocery List"
    )
    content = fields.String(
        required=True,
        description="Content of the note",
        example="Milk, Eggs, Bread"
    )


class NoteCreateSchema(NoteBaseSchema):
    """Schema for creating a note."""
    pass


class NoteUpdateSchema(Schema):
    """Schema for updating a note (partial allowed)."""
    title = fields.String(
        required=False,
        description="Updated title of the note",
        validate=validate.Length(min=1, max=200),
        example="Updated Grocery List"
    )
    content = fields.String(
        required=False,
        description="Updated content of the note",
        example="Milk, Eggs, Bread, Cheese"
    )


class NoteSchema(NoteBaseSchema):
    """Schema for returning a note."""
    id = fields.Integer(required=True, description="Unique identifier of the note", example=1)
    created_at = fields.DateTime(required=True, description="Creation timestamp (UTC)")
    updated_at = fields.DateTime(allow_none=True, description="Last updated timestamp (UTC) or null")
