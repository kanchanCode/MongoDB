import logging
logger=logging

logger.basicConfig(
filename='C:\\Users\\hp\\Desktop\\MongoDB\\Aggregation\\log_file.log',
filemode='w',
level=logging.INFO,
format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s'
)

logger.basicConfig(
filename='C:\\Users\\hp\\Desktop\\MongoDB\\Aggregation\\log_file.log',
filemode='w',
format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d'
)