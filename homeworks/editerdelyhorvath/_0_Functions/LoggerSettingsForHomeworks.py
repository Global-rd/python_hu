'''

Logger settings file a házifeladatokhoz alakítva OOP megoldással

'''

import logging
import os

class LoggerSettingsForHomeworks:
    """Logger settings class"""
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self._create_log_directory()
        self.logger = self._setup_logger()

    def _create_log_directory(self):
        log_dir = os.path.dirname(self.log_file_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print(f"Log directory created at: {log_dir}")

    def _setup_logger(self):
        logger = logging.getLogger("HomeworkLogger")

        # delete existing handlers, if any, to avoid duplicate messages
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.setLevel(logging.INFO)

        # File handler for detailed log
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - [Logged by: %(name)s]')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Stream handler for console log
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_formatter = logging.Formatter('%(levelname)s - %(message)s')
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

        print("Logger setup complete. Logging to", self.log_file_path)
        return logger

    def get_logger(self):
        return self.logger


