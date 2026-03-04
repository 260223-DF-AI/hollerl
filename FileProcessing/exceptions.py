class FileProcessingError(Exception):
    """Base exception for file processing errors."""
    def __init__(self, message="An error occurred while processing the file."):
        super().__init__(message)
        self.message = message

class InvalidDataError(FileProcessingError):
    """Raised when data validation fails."""
    def __init__(self, message="Error: Data validation failed."):
        super().__init__(message)
        self.message = message

class MissingFieldError(FileProcessingError):
    """Raised when a required field is missing."""
    def __init__(self, message="Error: A required field is missing."):
        super().__init__(message)
        self.message = message