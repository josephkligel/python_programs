import logging

logger = logging.Logger('My Logger')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('logfile.log', mode='w')
formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('This will get into the file.')
logger.info('Logger successfully created!')
logger.critical('Critical Message!')
