import logging
import json_log_formatter


def get_logger():

    formatter = json_log_formatter.JSONFormatter()

    json_handler = logging.StreamHandler()
    json_handler.setFormatter(formatter)

    logger = logging.getLogger("my_json")
    logger.addHandler(json_handler)
    logger.setLevel(logging.INFO)

    # logger.info('Sign up', extra={'referral_code': '52d6ce'})

    return logger


logger = get_logger()
