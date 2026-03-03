"""Tests for the Task model."""

import pytest
from task_manager.models.task import Task


class TestTask:
    """Test cases for the Task class."""
    
    def test_create_task_basic(self):
        """Test creating a basic task."""
        task = Task("Test Task")
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.completed is False
    
    def test_create_task_with_description(self):
        """Test creating a task with description."""
        task = Task("My Task", "This is a description")
        assert task.title == "My Task"
        assert task.description == "This is a description"
    
    def test_mark_complete(self):
        """Test marking a task complete."""
        task = Task("Test")
        assert task.completed is False
        task.mark_complete()
        assert task.completed is True
    
    def test_to_dict(self):
        """Test converting task to dictionary."""
        task = Task("Test Task", "Description")
        data = task.to_dict()
        
        assert data["title"] == "Test Task"
        assert data["description"] == "Description"
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data
    
    def test_str_representation(self):
        """Test string representation."""
        task = Task("My Task")
        assert "My Task" in str(task)
        assert "[ ]" in str(task)
        
        task.mark_complete()
        assert "[x]" in str(task)