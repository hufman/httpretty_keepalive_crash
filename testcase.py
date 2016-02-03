try:
	from urllib.parse import urlparse
except:
	from urlparse import urlparse

import httpretty
import re
import requests
import requests.adapters
import requests.packages.urllib3.connection

# a Request Session Adapter that doesn't do connection pooling
class NonPooledAdapter(requests.adapters.HTTPAdapter):
	def init_poolmanager(self, connections, maxsize, *args, **kwargs):
		self.poolmanager = FakePoolManager(num_pools=connections, maxsize=maxsize,
		                                   *args, **kwargs)

class FakePoolManager(requests.packages.urllib3.poolmanager.PoolManager):
	def _new_pool(self, scheme, host, port):
		return FakePool(host, port, self.connection_pool_kw)

class FakePool(requests.packages.urllib3.connectionpool.HTTPConnectionPool):
	def _get_conn(self, timeout=None):
		return self._new_conn()


def mock_server(request, uri, headers):
	return (200, {}, uri)

def test_case():
	httpretty.enable()
	httpretty.register_uri(httpretty.GET, 'http://example.com', body=mock_server)

	session = requests.Session()
	session.mount('http://example.com/', NonPooledAdapter())
	r = session.get('http://example.com/')
	r = session.get('http://example.com/')

	httpretty.disable()
	httpretty.reset()

if __name__ == '__main__':
	test_case()
