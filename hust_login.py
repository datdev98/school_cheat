import httplib, urllib
def login():
    conn = httplib.HTTPConnection('192.168.7.1')
    body = {'username': '',                         # Username here
            'password': '',                         # Password here
            'dst': 'http://www.hust.edu.vn/',
            'popup': 'true'
            }
    params = urllib.urlencode(body)
    conn.request('POST', '/login', params)
    res = conn.getresponse()
    data = res.read()
    print(data)

if __name__ == "__main__":
    login()
