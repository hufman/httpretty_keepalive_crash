import httpretty
import re
import requests

def mock_server(request, uri, headers):
	return (200, {}, uri)

def test_case():
	httpretty.enable()
	httpretty.register_uri(httpretty.GET, 'http://example.com', body=mock_server)

	session = requests.Session()
	r = session.get('http://example.com/')
	r = session.get('http://example.com/')

	httpretty.disable()
	httpretty.reset()

if __name__ == '__main__':
	test_case()
