import os
from interfaces.istrategy import IStrategy
from interfaces.ifilepath import IFilePathManager


class ConsoleLogStrategy(IStrategy):
    """Стратегия записи логов консоль"""

    def write(self, message: str):
        """Метод для вывода сообщения в консоль"""
        print(message)


class FileLogStrategy(IStrategy, IFilePathManager):
    """Стратегия записи логов в файл"""

    def __init__(self, file_path: str):
        """Инициализация экземпляра с указанным путем к файлу"""
        self.file_path = file_path

    def set_file_path(self, file_path: str):
        """Метод для установки нового пути к файлу для записи логов"""
        self.file_path = file_path

    def write(self, message: str):
        """Метод для записи сообщение в файл"""
        log_file_path = os.path.join(self.file_path, self.get_filename())
        with open(log_file_path, "a") as log_file:
            log_file.write(message + "\n")


class UpperCaseFileLogStrategy(FileLogStrategy):
    """Стратегия записи логов в файл с преобразованием текста в верхний регистр"""

    def set_file_path(self, file_path: str):
        """Метод для установки нового пути к файлу для записи логов"""
        super().set_file_path(file_path)

    def write(self, message: str):
        """Записывает сообщение в файл в верхнем регистре"""
        super().write(message.upper())
