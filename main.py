from libenum.level_message import LevelMessage
from logger import Logger
from strategies import ConsoleLogStrategy, FileLogStrategy, UpperCaseFileLogStrategy


file_path = "C:\\dp-2024-lab02\\logs"

logger = Logger(ConsoleLogStrategy())

logger.log(LevelMessage.INFO, "Старт")
logger.log(LevelMessage.WARN, "Внимание")
logger.log(LevelMessage.ERROR, "Ошибка")


file_log_strategy = FileLogStrategy(file_path)
logger.set_strategy(file_log_strategy)
logger.log(LevelMessage.INFO, "Старт записи в файл")
logger.log(LevelMessage.WARN, "Внимание! Старт записи в файл")
logger.log(LevelMessage.ERROR, "Ошибка!")


upper_case_file_log_strategy = UpperCaseFileLogStrategy(file_path)
upper_case_file_log_strategy.set_file_path(file_path + "\\uplogs")

logger.set_strategy(upper_case_file_log_strategy)
logger.log(LevelMessage.INFO, "старт")
logger.log(LevelMessage.WARN, "внимание!")
logger.log(LevelMessage.ERROR, "ошибка!")