from abc import ABC, abstractmethod

from src.core.genre.domain.genre import Genre


class GenreRepository(ABC):

    @abstractmethod
    def find_by_name(self, name: str) -> Genre:
        raise NotImplementedError
    
    @abstractmethod
    def save(self, genre: Genre) -> Genre:
        raise NotImplementedError