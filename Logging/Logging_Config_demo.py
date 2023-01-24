import logging
import logging.config

class LogConfig():

    logging.config.fileConfig('logging_Config')

    logger = logging.getLogger(LogConfig.__name__)
    logger.setLevel(logging.INFO)






    logger.info("info")
    logger.warning("warning")
    logger.error("error")