# Python program to validate an Email
import logging
import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# Define a function for
# for validating an Email


def check_email(email):
    # pass the regular expression
    # and the string in search() method
    if re.match(regex, email):
        return True, None
    else:
        err_msg = "Invalid Email {}".format(email)
        logging.WARN(err_msg)
        err_payload = {
            "code": 400,
            "message": err_msg
        }
        return False, err_payload