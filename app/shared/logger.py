import logging
import sys


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )

    return logging.getLogger("forgeos")