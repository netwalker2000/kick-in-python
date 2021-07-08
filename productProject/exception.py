import logging


class CustomizedException(object):
    def __init__(self):
        logging.info("__init__")

    def process_exception(self, request, exception):
        logging.info("Customized Exception: {}".format(exception))
        err_payload = {
            "code": 500,
            "message": "Customized Exception Handler, please check server log"
        }
        return err_payload
