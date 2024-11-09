import logging

def create_file_handler(logfile,level):
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(level)
    return file_handler

def create_stream_handler(level):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    return stream_handler

def set_formatter(handler):
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
    handler.setFormatter(log_format)

def setup_logger(name, logfile="homeworks/nagynorbert/4_exceptions_logging/tasks_log.log",level=logging.INFO,handlers=None):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if handlers is None:
        handlers = ["stream", "file"]

    for handler in handlers:
        match handler:
            case "stream":
                stream_handler = create_stream_handler(level)
                set_formatter(stream_handler)
                logger.addHandler(stream_handler)
            case "file":
                file_handler = create_file_handler(logfile,level)
                set_formatter(stream_handler)
                logger.addHandler(file_handler)
            case _:
                print("Unexpected event during log settings.")
    
    return logger

