"""Formatting utilities for the task manager."""

from datetime import datetime
from typing import List

# Try to import colorama for colored output
try:
    from colorama import Fore, Style, init
    init()
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False


def format_date(dt: datetime) -> str:
    """
    Format a datetime object to a readable string.
    
    Args:
        dt: The datetime to format
        
    Returns:
        Formatted date string
    """
    return dt.strftime("%Y-%m-%d %H:%M")


def format_task_list(tasks: List) -> str:
    """
    Format a list of tasks for display.
    
    Args:
        tasks: List of Task objects
        
    Returns:
        Formatted string representation
    """
    if not tasks:
        return "No tasks found."
    
    lines = ["=" * 40]
    lines.append("TASK LIST")
    lines.append("=" * 40)
    
    for task in tasks:
        if HAS_COLOR:
            if task.completed:
                status = f"{Fore.GREEN}[DONE]{Style.RESET_ALL}"
            else:
                status = f"{Fore.YELLOW}[TODO]{Style.RESET_ALL}"
        else:
            status = "[DONE]" if task.completed else "[TODO]"
        
        lines.append(f"{status} {task.id}. {task.title}")
        
        if task.description:
            lines.append(f"      {task.description[:50]}...")
    
    lines.append("=" * 40)
    lines.append(f"Total: {len(tasks)} tasks")
    
    return "\n".join(lines)


def format_task_detail(task) -> str:
    """
    Format a single task with full details.
    
    Args:
        task: The Task object to format
        
    Returns:
        Detailed formatted string
    """
    status = "Completed" if task.completed else "Pending"
    created = format_date(task.created_at)
    
    return f"""
Task #{task.id}
-----------
Title: {task.title}
Status: {status}
Created: {created}
Description: {task.description or 'No description'}
""".strip()