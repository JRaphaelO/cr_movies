from dataclasses import dataclass, field
import uuid
from uuid import UUID

@dataclass
class Genre:
    name: str
    description: str = ""
    is_active: bool = True
    id: UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        self.validate()
    
    def validate(self):
        if len (self.name) > 255:
            raise ValueError("Genre name is too long (max 255 characters)")
        
        if not self.name:
            raise ValueError("Genre name is required")

    def __str__(self):
        return f"{self.name} - {self.description} ({self.is_active})"
    
    def __repr__(self):
        return f"{self.name} - {self.description} ({self.is_active})"
    
    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        
        return self.id == other.id
    
    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def update(self, name: str, description: str):
        self.name = name
        self.description = description
        self.validate()
