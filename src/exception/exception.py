"""Custom application exceptions."""


class DocumentNotFoundError(Exception):
    """Raised when a required document (resume or personal doc) cannot be found."""

    def __init__(self, document_name: str):
        self.document_name = document_name
        super().__init__(f"Document not found: {document_name}")


class DocumentParseError(Exception):
    """Raised when a document exists but cannot be parsed/read."""

    def __init__(self, document_name: str, reason: str = ""):
        self.document_name = document_name
        self.reason = reason
        super().__init__(f"Failed to parse document '{document_name}': {reason}")


class LLMResponseError(Exception):
    """Raised when the LLM fails to return a valid response."""

    def __init__(self, reason: str = ""):
        self.reason = reason
        super().__init__(f"LLM response error: {reason}")


class DataNotLoadedError(Exception):
    """Raised when the application state data has not been loaded yet."""

    def __init__(self):
        super().__init__("Application data is not loaded. Server may still be starting up.")


class FileNotFoundError(Exception):
    def __init__(self,file_name:str):
        print("gtfgbtghbtgbtgbtibg")
        self.file_name=file_name
        super.__init__(f"The {file_name} not found")
        