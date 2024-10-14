import setup_logger

logger = setup_logger.setup_logger("root_logger")

logger.info("This is our first log")
logger.error("This is an error message")