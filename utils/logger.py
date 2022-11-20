import logging
import os

log_file_name = os.path.join(
    __name__, os.pardir, "log/", "development.log")


# logging.basicConfig(filename=log_file_location, format='%(filename)s: %(message)s',
#                     level=logging.INFO)

logger = logging.getLogger()

log_formatter = logging.Formatter( "[%(levelname)-5.5s]  [%(filename)s]  %(message)s")

file_handler = logging.FileHandler(log_file_name)
file_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

logger.addHandler(console_handler)

logger.setLevel(logging.DEBUG)