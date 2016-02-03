import httpretty
import re
import requests

def test_case():
	httpretty.enable()
	httpretty.register_uri(httpretty.GET, 'http://example.com', body='yay')

	session = requests.Session()
	r = session.get('http://example.com/')
	r = session.get('http://example.com/')

	httpretty.disable()
	httpretty.reset()

if __name__ == '__main__':
	test_case()
