import os
import logging

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

logger = logging.getLogger("Theme prediction model")
logger.setLevel(logging.DEBUG)

stdout_logger = logging.StreamHandler()
stdout_logger.setFormatter(
    logging.Formatter(
        '[%(name)s:%(filename)s:%(lineno)d] - [%(process)d] - %(asctime)s - %(levelname)s - %(message)s'
    )
)

logger.addHandler(stdout_logger)

# Add any other configurations specific to your theme model
