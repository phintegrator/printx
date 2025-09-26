import inspect
import logging
import os
import sys

def get_default_log_filename():
    frame = inspect.currentframe()
    caller_frame = None
    try:
        caller_frame = frame.f_back if frame else None
        source_file = caller_frame.f_code.co_filename if caller_frame else None
    finally:
        del frame
        if caller_frame is not None:
            del caller_frame
    if not source_file or source_file in ('<stdin>', '<string>'):
        source_file = sys.argv[0] if sys.argv and sys.argv[0] else __file__
    base_name = os.path.splitext(os.path.basename(source_file))[0]
    return f"{base_name}.log"

def printx_configure(log_filename=None, level=logging.DEBUG):
    if log_filename is None:
        log_filename = get_default_log_filename()

    logging.basicConfig(level=level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(log_filename),
                            logging.StreamHandler()
                        ])

def printx(*args, log_level='info', **kwargs):
    message = ' '.join(map(str, args))

    if log_level == 'debug':
        logging.debug(message)
    elif log_level == 'info':
        logging.info(message)
    elif log_level == 'warning':
        logging.warning(message)
    elif log_level == 'error':
        logging.error(message)
    elif log_level == 'critical':
        logging.critical(message)
    else:
        logging.info(message)
