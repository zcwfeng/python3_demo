import logging


class CustomLogger:
    logger = None

    @staticmethod
    def init_log(output=None):
        """
        Initialise the logger
        """
        CustomLogger.logger = logging.getLogger('BitcoinExchangeFH')
        CustomLogger.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s \n%(message)s\n')
        if output is None:
            slogger = logging.StreamHandler()
            slogger.setFormatter(formatter)
            CustomLogger.logger.addHandler(slogger)
        else:
            flogger = logging.FileHandler(output)
            flogger.setFormatter(formatter)
            CustomLogger.logger.addHandler(flogger)

    @staticmethod
    def info(method, str):
        """
        Write info log
        :param method: Method name
        :param str: Log message
        """
        CustomLogger.logger.info('[%s]\n%s\n' % (method, str))

    @staticmethod
    def error(method, str):
        """
        Write info log
        :param method: Method name
        :param str: Log message
        """
        CustomLogger.logger.error('[%s]\n%s\n' % (method, str))
