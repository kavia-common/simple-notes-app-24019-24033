"""
Domain models for the Notes application.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Note:
    """
    Represents a Note entity in the system.
    """
    id: int
    title: str
    content: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
