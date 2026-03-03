from datetime import datetime
from typing import Optional


class Task:
    """Represents a task in the task manager."""
    
    _id_counter = 0
    
    def __init__(
        self, 
        title: str, 
        description: str = "", 
        completed: bool = False
    ):
        """
        Initialize a new Task.
        
        Args:
            title: The task title (required)
            description: Optional task description
            completed: Whether the task is completed
        """
        Task._id_counter += 1
        self.id = Task._id_counter
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
    
    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True
    
    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False
    
    def to_dict(self) -> dict:
        """
        Convert task to dictionary representation.
        
        Returns:
            Dictionary with task data
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }
    
    def __str__(self) -> str:
        """Return formatted string representation."""
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id}. {self.title}"
    
    def __repr__(self) -> str:
        """Return detailed representation."""
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"