from abc import ABC as ABS, abstractmethod

class BaseUseCase(ABS):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
