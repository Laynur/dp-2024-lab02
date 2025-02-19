import threading


class Singleton:
    """Паттерн Singleton"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        Создает и возвращает единственный экземпляр класса.
        Использует блокировку для защиты от многократного создания
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance