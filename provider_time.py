from datetime import datetime


class ProviderTime:
    """Класс для предоставления времени"""

    @staticmethod
    def get_time_in_message():
        """Метод который возвращает время в формате %Y-%m-%d %H:%M:%S """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_time_in_filename():
        """Метод который возвращает время в формате %Y-%m-%d %H:%M:%S """
        return datetime.now().strftime("%Y-%m-%d.%H-%M-%S")