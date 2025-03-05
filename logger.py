import threading
from interfaces.ilogger import ILogger
from interfaces.istrategy import IStrategy
from libenum.level_message import LevelMessage
from provider_time import ProviderTime
from singleton import Singleton


class Logger(Singleton, ILogger):
    """Логгер с возможностью смены стратегии записи"""

    _lock = threading.Lock()

    def __init__(self, strategy: IStrategy):
        """Инициализация логгера с заданной стратегией записи"""
        self.strategy = strategy

    def set_strategy(self, strategy: IStrategy):
        """Метод для установки новой стратегий записи для логера"""
        self.strategy = strategy

    def _format_message(self, level:str, message:str):
        """Метод для форматирования сообщения с временем и уровнем логирования"""
        return f"{ProviderTime.get_time_in_message()} [{level}] {message}"

    def log(self, level: LevelMessage, message:str):
        """Метод логирования сообщения с указаннным уровнем логирования"""
        format_message = self._format_message(level.value, message)
        with self._lock:
            self.strategy.write(format_message)
