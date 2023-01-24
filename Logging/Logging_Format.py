import logging

class LoggingHandler():

    def test(self):

        logger = logging.getLogger(LoggingHandler.__name__)
        logger.setLevel(level=logging.INFO)

        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s, %(name)s,%(levelname)s : %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

        c_handler.setFormatter(formatter)
        logger.addHandler(c_handler)

        logger.info("info")
        logger.warning("warning")
        logger.error("error")

demo = LoggingHandler()
demo.test()
