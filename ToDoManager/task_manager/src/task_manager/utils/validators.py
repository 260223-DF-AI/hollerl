"""Validation utilities for the task manager."""


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def validate_title(title: str) -> str:
    """
    Validate a task title.
    
    Args:
        title: The title to validate
        
    Returns:
        The cleaned title
        
    Raises:
        ValidationError: If title is invalid
    """
    if not title:
        raise ValidationError("Title cannot be empty")
    
    title = title.strip()
    
    if len(title) == 0:
        raise ValidationError("Title cannot be only whitespace")
    
    if len(title) > 100:
        raise ValidationError("Title must be 100 characters or less")
    
    return title


def validate_description(description: str) -> str:
    """
    Validate a task description.
    
    Args:
        description: The description to validate
        
    Returns:
        The cleaned description
    """
    if description is None:
        return ""
    
    description = description.strip()
    
    if len(description) > 500:
        raise ValidationError("Description must be 500 characters or less")
    
    return description