from abc import ABC, abstractmethod


class IStrategy(ABC):
    """Интерфейс для стратегий записи логов"""
    @abstractmethod
    def write(self, message: str):
        """Записывает сообщение в соответствующий выходной поток"""
        pass