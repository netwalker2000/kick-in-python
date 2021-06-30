class CustomError(Exception):
    status_code = None

    def get_status_code(self):
        if self.status_code is None:
            raise Exception
        return self.status_code


class UnknownError(CustomError):
    status_code = 500
