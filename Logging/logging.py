import logging

logger = logging.getLogger('finance_module_logger')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('finance.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.debug('This is a debug message from the custom logger')
