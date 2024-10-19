import logging

def create_file_handler(log_file, level=logging.DEBUG):
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    return file_handler

def create_stream_handler(level=logging.INFO):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    return stream_handler

# A függvény most már elfogadja a detailed argumentumot
def set_formatter(handler, detailed=False):
    if detailed:
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - [Logged by: %(name)s]')
    else:
        log_format = logging.Formatter('%(levelname)s - %(message)s')  # Egyszerű formázás a terminálhoz
    handler.setFormatter(log_format)

def setup_logger(name, log_file="logs/my_custom_log.log", level=logging.DEBUG, handlers=None):

    logger = logging.getLogger(f"My app: {name}")  # Custom logger name
    logger.setLevel(level)

    if handlers is None:
        handlers = ['file', 'stream']
    
    for handler in handlers:
        if handler == 'file':
            file_handler = create_file_handler(log_file, level)
            set_formatter(file_handler, detailed=True)  # detailed log for log file
            logger.addHandler(file_handler)
        elif handler == 'stream':
            stream_handler = create_stream_handler(logging.INFO)
            set_formatter(stream_handler, detailed=False)  # simple log for terminal
            logger.addHandler(stream_handler)
    
    return logger

