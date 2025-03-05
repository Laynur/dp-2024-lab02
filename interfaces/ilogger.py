from abc import ABC, abstractmethod
from interfaces.istrategy import IStrategy


class ILogger(ABC):
    """Интерфейс для логгера, определяющий основные методы для настройки и записи логов"""

    @abstractmethod
    def set_strategy(self, strategy: IStrategy):
        """Метод для установки стретегии записи логов"""
        pass

    def log(self, level: str, message: str):
        """Метод для записи сообщения с указанным уровнем логирования"""
        pass
