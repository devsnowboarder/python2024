import logging


class BaseClass:

    def test_loggingDemo(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        logging.Formatter("%(asctime)s :%(kevekbane)s : %(name)s :%(message)s")
        logger.addHandler(fileHandler)
        logger.debug(" A debug statement is executed")
        logger.info("Information statement")
        logger.warning(" something is in warning mode")
        logger.error(" a Major error has happened")
        logger.critical(" Critical issue")
        return logger
