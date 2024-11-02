'''

Kivételek kezeléséhez OOP-nál, hogy tudjuk az egyedi hibaüzeneteket megadni, és egy kezdő érték a napló fileokhoz.

'''

import os
from LoggerSettingsForHomeworks import LoggerSettingsForHomeworks

# Set up default log path
current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, 'logs')
log_file_path = os.path.join(log_dir, 'exceptions.log')

# Initialize logger settings
logger_settings = LoggerSettingsForHomeworks(log_file_path)
logger = logger_settings.get_logger()


class InvalidAmountError(Exception):
    """ Custom exception for invalid errors"""
    
    def __init__(self, message, logger=None):
        super().__init__(message)

