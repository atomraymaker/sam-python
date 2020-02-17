import logging
import os
import sys

import structlog
from structlog.processors import JSONRenderer, TimeStamper
from structlog.stdlib import LoggerFactory

if os.getenv("AWS_EXECUTION_ENV", "").startswith("AWS_"):
    logging.basicConfig(
        format="%(message)s", filename="/tmp/local.log", level=logging.DEBUG
    )
elif os.getenv("LOGLEVEL", "INFO") == "DEBUG":
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.DEBUG)
elif os.getenv("LOGLEVEL", "INFO") == "WARNING":
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.WARNING)
else:
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)

if os.getenv("AWS_EXECUTION_ENV", "").startswith("AWS_"):
    structlog.configure(
        logger_factory=LoggerFactory(),
        processors=[
            structlog.stdlib.add_log_level,
            TimeStamper(utc=True),
            structlog.dev.ConsoleRenderer(),
        ],
    )
else:
    structlog.configure(
        logger_factory=LoggerFactory(),
        processors=[
            structlog.stdlib.add_log_level,
            TimeStamper(utc=True),
            JSONRenderer(sort_keys=True),
        ],
    )

LOG = structlog.get_logger()
