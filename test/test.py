import os
import unittest
from unittest.mock import mock_open, patch
from strategies import ConsoleLogStrategy, FileLogStrategy, UpperCaseFileLogStrategy


class TestConsoleLogStrategy(unittest.TestCase):
    @patch('builtins.print')
    def test_write_logs_to_console(self, mock_print):
        console_strategy = ConsoleLogStrategy()
        console_strategy.write("Test")
        mock_print.assert_called_once_with("Test")


class TestFileLogStrategy(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_write_logs_to_file(self, mock_file):
        file_log_strategy = FileLogStrategy('test_log')
        file_log_strategy.write("Привет")

        expected_path = os.path.join('test_log', file_log_strategy.get_filename())
        mock_file.assert_called_once_with(expected_path, 'a')
        mock_file().write.assert_called_once_with("Привет\n")


class TestUpperCaseFileLogStrategy(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_write_logs_in_upper_case(self, mock_file):
        writer = UpperCaseFileLogStrategy('test_log')
        writer.write("привет")

        # Создание пути для проверки
        expected_path = os.path.join('test_log', writer.get_filename())

        # Проверка, что файл открывается с правильными параметрами
        mock_file.assert_called_once_with(expected_path, 'a')

        # Проверка, что сообщение записывается в файл в верхнем регистре
        mock_file().write.assert_called_once_with("ПРИВЕТ\n")
