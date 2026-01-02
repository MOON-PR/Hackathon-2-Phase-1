from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field

@dataclass
class Todo:
    """
    Represents a todo item with ID, title, description, status, and creation timestamp.
    """
    id: int
    title: str
    description: Optional[str] = None
    status: str = "pending"
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty or whitespace only")

        if self.status not in ["pending", "completed"]:
            raise ValueError(f"Status must be 'pending' or 'completed', got '{self.status}'")

        if len(self.title) > 200:
            raise ValueError("Title must be 200 characters or less")

        if self.description and len(self.description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

    def to_dict(self) -> dict:
        """Convert the Todo to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Todo from a dictionary representation."""
        # Parse the datetime string back to datetime object
        if "created_at" in data:
            created_at = datetime.fromisoformat(data["created_at"])
        else:
            created_at = datetime.now()

        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description"),
            status=data.get("status", "pending"),
            created_at=created_at
        )