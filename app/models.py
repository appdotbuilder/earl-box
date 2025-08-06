from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class UploadedFile(SQLModel, table=True):
    """Model for tracking uploaded files in the Earl Box application."""

    __tablename__ = "uploaded_files"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str = Field(max_length=255, index=True)
    original_filename: str = Field(max_length=255)
    file_path: str = Field(max_length=500)
    file_size: int = Field(ge=0)  # File size in bytes
    mime_type: str = Field(max_length=100)
    upload_timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)  # Soft delete flag


class FileUploadRequest(SQLModel, table=False):
    """Schema for validating file upload requests."""

    filename: str = Field(max_length=255)
    file_size: int = Field(ge=0)
    mime_type: str = Field(max_length=100)


class FileResponse(SQLModel, table=False):
    """Schema for file response data."""

    id: int
    filename: str
    original_filename: str
    file_size: int
    mime_type: str
    upload_timestamp: str  # ISO format datetime string
    download_url: str
