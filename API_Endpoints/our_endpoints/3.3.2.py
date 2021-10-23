import requests
URL = 'https://www.google.com'
res = requests.get(url=URL)
print(res)
if res.status_code == 200:
    print(res.headers)
else:
    print(res.status_code)

import requests

class GetRequests:
    def make_get_request(self, url):
        res = requests.get(url=url)

        if res.status_code == 200:
            print(res.headers)
        else:
            print(res.status_code)


urls = {'google': 'https://www.google.com'}

my_get = GetRequests()
my_get.make_get_request(urls['google'])
