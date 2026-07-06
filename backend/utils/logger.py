import logging
import os


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger:

            return cls._logger

        os.makedirs("data/logs", exist_ok=True)

        logger = logging.getLogger("JARVIS")

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            "data/logs/jarvis.log",
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        cls._logger = logger

        return logger