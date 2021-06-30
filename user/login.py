import time
from datetime import datetime

from productProject import settings
from user.config import REGISTRATION_REQUEST_ID
from user.connection import TcpPersistentConnectionPool


def user_login(name, password):
    # Construct request
    r_string = '{"Name":"login","Args":["' + name + '","' + password + '"]}'
    payload = bytes(r_string)

    tcp_pool = TcpPersistentConnectionPool.instance()
    with tcp_pool.connection() as tcp_connection:
        tcp_connection.send_request(REGISTRATION_REQUEST_ID, payload)
        data = tcp_connection.recv_response()
        # todo : deal with response
        # if go service said yes
        res = True
        if res:
            print("Yes")
            token = make_token(name)
            return token
        else:
            print("No")
            return "None"

def make_token(name):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    # with timestamp return back to user fe, fe store the token to cookies
    str = name + timestampStr # future, add other such as id if it is necessary
    secret_of_host = settings.SECRET_OF_TOKEN
    token = hash(hash(str + secret_of_host)) # double hash protection
    return token
