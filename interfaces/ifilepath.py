from abc import ABC, abstractmethod
from provider_time import ProviderTime

class IFilePathManager(ABC):
    """Интерфейс для управления путями к файлам логов"""

    @abstractmethod
    def set_file_path(self, file_path: str):
        """Метод для устанавки путь к файлу для записи логов"""
        pass

    @staticmethod
    def get_filename():
        """Метод для генерации имени файла лога с текущим временем"""
        return f"DP.P1.{ProviderTime.get_time_in_filename()}.log"