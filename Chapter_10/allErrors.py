import logging
logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Debugging information.')
logging.info('Logging module works.')
logging.warning('Risk of receiving an error message')
logging.error('An error occurred')
logging.critical('It is impossible to restore the operation of the application')
