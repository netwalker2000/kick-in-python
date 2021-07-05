import time
from datetime import datetime

import gevent

from productProject import settings
from user.config import REGISTRATION_REQUEST_ID
from user.connection import TcpPersistentConnectionPool


def user_login(name, password, apply_timestamp=1625213873):
    # Construct request
    r_string = '{"Name":"login","Args":["' + name + '","' + password + '"]}'
    combined_string = '[' + r_string
    for i in range(0):
        combined_string += "," + r_string
    combined_string += "]"
    # print(combined_string)
    payload = bytes(combined_string)

    tcp_pool = TcpPersistentConnectionPool.instance()
    sock_fd = gevent.socket.create_connection(tcp_pool.address)
    with tcp_pool.connection() as tcp_connection:
        tcp_connection.send_request(REGISTRATION_REQUEST_ID, payload, sock_fd)
        data = tcp_connection.receive_response(sock_fd)
        # print(data)
        # todo : deal with response
        # if go service.py said yes
        res = True
        if res:
            # print("Yes")
            token = make_token(name, apply_timestamp)
            return token
        else:
            # print("No")
            return "None"


def validate_token(name, apply_timestamp, token):
    curr_timestamp= datetime.now()
    # print(curr_timestamp)
    # todo: check the apply_timestamp and current time, shouldn't be expired
    str_raw = name + str(apply_timestamp)
    secret_of_host = settings.SECRET_OF_TOKEN
    # calc token and compare
    regenerated_token = str(hash(hash(str_raw + secret_of_host)))
    # print(token + "[original], while regenerated Token:")
    # print(regenerated_token)
    if token != regenerated_token:
        return False
    return True


def make_token(name, apply_timestamp):
    approval_timestamp = datetime.now()
    # print(approval_timestamp)
    # todo: check the apply_timestamp and approval_timestamp, shouldn't be too different
    # with timestamp return back to user fe, fe store the token to cookies
    # future, add other such as id if it is necessary
    str_raw = name + str(apply_timestamp)
    secret_of_host = settings.SECRET_OF_TOKEN
    # double hash protection
    token = hash(hash(str_raw + secret_of_host))
    return token
