import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="log.log",
                    filemode='w')

# logging.debug("this is debug message")
# logging.info("this is info message")
# logging.warning("this is warning message")
# logging.error("this is error message")
# logging.critical("this is critical message")