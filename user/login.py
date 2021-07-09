import functools
import hashlib

from datetime import datetime
from django.core.cache import cache

from productProject import settings
from user.config import REGISTRATION_REQUEST_ID
from user.connection import TcpPersistentConnectionPool


def login_cache_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = args[0]
        password = args[1]
        try:
            cached_pw = cache.get("name_pw_%s" % name)
        except:
            pass
        if cached_pw != "" and safe_hash(password) == cached_pw:
            token = cache.get("name_token_%s" % name)
        else:
            token = func(name, password)
            if token != "None":
                cache.set("name_pw_%s" % name, safe_hash(password), settings.CACHE_TIMEOUT)
                cache.set("name_token_%s" % name, token, settings.CACHE_TIMEOUT)
        return token
    return wrapper


@login_cache_decorator
def user_login(name, password, apply_timestamp=1625213873):
    # Construct request
    r_string = '{"Name":"login","Args":["' + name + '","' + password + '"]}'
    combined_string = '[' + r_string
    combined_string += "]"
    payload = bytes(combined_string)

    tcp_pool = TcpPersistentConnectionPool.instance()
    with tcp_pool.connection() as tcp_connection:
        tcp_connection.send_request(REGISTRATION_REQUEST_ID, payload)
        res = tcp_connection.receive_response()
        # todo : deal with response
        # if go service.py said yes
        if res is not None:
            token = make_token(name, apply_timestamp)
            return token
        else:
            return "None"


def login_validate_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        name = request.GET["name"]
        apply_timestamp = request.GET["apply_timestamp"] # header
        token = request.GET["token"] #header
        if validate_token(name, apply_timestamp, token):
            return func(*args, **kwargs)
        else:
            raise Exception("Authentication failed")
    return wrapper


def validate_token(name, apply_timestamp, token):
    curr_timestamp = datetime.now()
    # todo: check the apply_timestamp and current time, shouldn't be expired
    str_raw = name + str(apply_timestamp)
    secret_of_host = settings.SECRET_OF_TOKEN
    # calc token and compare
    regenerated_token = safe_hash(safe_hash(str_raw + secret_of_host))
    if token != regenerated_token:
        return False
    return True


def make_token(name, apply_timestamp):
    approval_timestamp = datetime.now()
    # todo: check the apply_timestamp and approval_timestamp, shouldn't be too different
    # with timestamp return back to user fe, fe store the token to cookies
    # future, add other such as id if it is necessary
    str_raw = name + str(apply_timestamp)
    secret_of_host = settings.SECRET_OF_TOKEN
    # double hash protection
    token = safe_hash(safe_hash(str_raw + secret_of_host))
    return token


def safe_hash(input_text):
    crypto_hash = hashlib.sha256()
    crypto_hash.update(input_text)
    return crypto_hash.hexdigest()
