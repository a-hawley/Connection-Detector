from http.client import HTTPConnection
from urllib.parse import urlparse


def online(url, timeout=3):
    error = Exception('unknown error')
    parser = urlparse(url)
    host = parser.netloc or parser.path.split('/')[0]
    print(parser.netloc)

    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request('HEAD', '/')
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error
