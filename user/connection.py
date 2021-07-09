import logging
import struct

import gevent.socket
import gevent.queue
import gevent.lock
from django.conf import settings

from utils.errors import UnknownError

tcp_setting = settings.TCP_SERVERS["localhost"]


class TcpPersistentConnection(object):
	def __init__(self, sock_fd, pool):
		self.pool = pool
		self.sock_fd = sock_fd

		self.receive = self.sock_fd.recv
		self.sendall = self.sock_fd.sendall
		self.send = self.sock_fd.send

	def __enter__(self):
		return self

	def __exit__(self, exception_type, exception_value, exception_traceback):
		if exception_traceback:
			# Replace socket connection
			logging.debug("Closing connection due to exception")
			# self.pool.keep_alive_queue.put_nowait(None)
			# self.pool.connection_count.release()
			self.sock_fd.close()
			return

		# Return the socket
		self.sock_fd.close()
		logging.debug("Releasing connection")
		# self.pool.keep_alive_queue.put_nowait(self.sock_fd)
		# self.pool.connection_count.release()

	def send_request(self, request_id, payload_bytearray):
		logging.debug("Sending binaries for request id %d", request_id)
		raw_message_length = len(payload_bytearray)
		# print("raw_message_length: %d" % raw_message_length)
		payload_bytearray = struct.pack('>I', raw_message_length) + payload_bytearray
		self.sendall(payload_bytearray)
		logging.info("Sent %d bytes", len(payload_bytearray))

	def receive_response(self):
		# Read message length and unpack it into an integer
		logging.debug("Receiving payload length")
		raw_message_length = self.receive_all(4)
		if raw_message_length == 0:
			return None
		message_length = struct.unpack('>I', raw_message_length)[0]
		if message_length == 0:
			return None
		# Read the message data
		return self.receive_all(message_length)

	def receive_all(self, n):
		logging.debug("Receiving payload of %d bytes", n)
		data = bytearray()
		while len(data) < n:
			with gevent.Timeout(tcp_setting["TCP_TIMEOUT_SECONDS"], False):
				try:
					packet_inner = self.receive(n - len(data))
				except Exception as e:
					logging.error(e)
					# raise UnknownError("Internal server error")
			data.extend(packet_inner)
		return data


class TcpPersistentConnectionPool(object):
	def __init__(self):
		logging.debug("TcpPersistentConnectionPool init called")
		raise UnknownError("Internal server error")

	def connection(self):
		logging.debug("Obtaining connection")
		sock_fd = gevent.socket.create_connection(self.address)
		# self.connection_count.acquire()
		# sock_fd = self.keep_alive_queue.get()
		# if sock_fd is None:
		# 	sock_fd = gevent.socket.create_connection(self.address)
		return TcpPersistentConnection(sock_fd, self)

	@classmethod
	def instance(cls):
		if not hasattr(cls, '_instance'):
			logging.debug("Initializing connection pool")
			cls._instance = cls.__new__(cls)
			cls._instance.address = (tcp_setting["TCP_HOST"], tcp_setting["TCP_PORT"])
			cls._instance.pool_size = tcp_setting["TCP_NUM_CONNECTIONS"]
			cls._instance.connection_count = gevent.lock.BoundedSemaphore(tcp_setting["TCP_NUM_CONNECTIONS"])
			cls._instance.keep_alive_queue = gevent.queue.Queue(tcp_setting["TCP_NUM_CONNECTIONS"])
			try:
				logging.info("instance init conns")
				for _ in xrange(cls._instance.pool_size):
					cls._instance.keep_alive_queue.put_nowait(gevent.socket.create_connection(cls._instance.address))
			except Exception as e:
				logging.error(e)
				del cls._instance
				raise UnknownError("Internal server error")
			logging.info("Connection pool instance initialized")
		return cls._instance
