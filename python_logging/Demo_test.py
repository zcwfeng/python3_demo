from python_logging.Demo_CustomLogger import CustomLogger

CustomLogger.init_log()
# CustomLogger.info()
log_str = '%s/%s/%s\n' % ("demo1", "demo2", "demo3")
CustomLogger.info('[main]', log_str)

