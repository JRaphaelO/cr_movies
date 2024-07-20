from abc import ABC, abstractmethod

from src.core.genre.domain.genre import Genre


class GenreRepository(ABC):

    @abstractmethod
    def save(self, genre: Genre) -> Genre:
        raise NotImplementedError
    
    @abstractmethod
    def list(self) -> list[Genre]:
        raise NotImplementedError
    
    def update(self, genre: Genre) -> Genre:
        raise NotImplementedError
    
    @abstractmethod
    def find_by_name(self, name: str) -> Genre:
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, id: int) -> Genre:
        raise NotImplementedError