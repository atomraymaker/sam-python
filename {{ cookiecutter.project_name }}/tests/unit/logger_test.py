import imp
import os

import logger


def test_aws():
    os.environ["AWS_EXECUTION_ENV"] = "AWS_"
    imp.reload(logger)
    logger.LOG.info("test")
    os.environ["AWS_EXECUTION_ENV"] = ""


def test_debug():
    os.environ["LOGLEVEL"] = "DEBUG"
    imp.reload(logger)
    logger.LOG.info("test")
    os.environ["LOGLEVEL"] = ""


def test_warning():
    os.environ["LOGLEVEL"] = "WARNING"
    imp.reload(logger)
    logger.LOG.info("test")
    os.environ["LOGLEVEL"] = ""
