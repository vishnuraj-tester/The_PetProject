import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(name= __name__):
    logger = logging.getLogger(name)

    if not logger.handlers: #prevents duplicate logs
        logger.setLevel(logging.DEBUG)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(project_root, "reports", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, "test_log.log")
    #handlers
        console_handler = logging.StreamHandler()
        file_handler = RotatingFileHandler(log_file_path, maxBytes=3000000, backupCount=3)
    #formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    #adding handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger