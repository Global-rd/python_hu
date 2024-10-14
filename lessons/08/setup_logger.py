import logging

def create_file_handler(log_file, level):
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    return file_handler

def create_stream_handler(level):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    return stream_handler

def set_formatter(handler):
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
    handler.setFormatter(log_format)


def setup_logger(name, log_file="lessons/08/app.log", level=logging.INFO, handlers=None):

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if handlers is None:
        handlers = ['file', 'stream']
    
    for handler in handlers:
        if handler == 'file':
            file_handler = create_file_handler(log_file, level)
            set_formatter(file_handler)
            logger.addHandler(file_handler)
        elif handler == 'stream':
            stream_handler = create_stream_handler(level)
            set_formatter(stream_handler)
            logger.addHandler(stream_handler)
    
    return logger
