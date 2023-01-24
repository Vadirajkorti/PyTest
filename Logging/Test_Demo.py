import logging

#logging.basicConfig(filename='test.log',level=logging.DEBUG)
logging.basicConfig( format="%(asctime)s,%(levelname)s : %(message)s",datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.info("info")
logging.warning("warning")
logging.error("error")