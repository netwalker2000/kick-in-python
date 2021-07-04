from user.config import REGISTRATION_REQUEST_ID
from user.connection import TcpPersistentConnectionPool


def register_user(name, password, email):
    # Construct request
    r_string = '{"Name":"register","Args":["' + name + '","' + password + '","' + email + '"]}'
    payload = bytes(r_string)
    tcp_pool = TcpPersistentConnectionPool.instance()
    with tcp_pool.connection() as tcp_connection:
        tcp_connection.send_request(REGISTRATION_REQUEST_ID, payload)
        data = tcp_connection.receive_response()
        # todo : deal with response
        print(data)
        return data

