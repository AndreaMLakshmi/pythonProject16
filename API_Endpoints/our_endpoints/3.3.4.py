import requests
class GetRequests:
    @classmethod
    def print_response_headers(self, response_headers):
        for key, value in response_headers.items():
            print(key, ": ", value)

    @classmethod
    def make_get_request(self, url, params=None, headers=None):
        return requests.get(url=url, params=params, headers=headers)

        if res.status_code == 200:
            self.print_response_headers(res.headers)
        else:
            self.print_response_headers(res.status_code)


urls = {'google': 'https://www.google.com', 'httpbin': {'url': 'https://httpbin.org', 'uri': ('get', 'response-headers')}}
gr = GetRequests()
resp = gr.make_get_request(urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][0])
print(resp)
params_get = {'freeform': 'Something is HERE'}
headers_get = {'content-type': 'application/json'}

gr = GetRequests()
resp = gr.make_get_request(urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][1], params=params_get, headers=headers_get)
print(gr.print_response_headers(resp.headers))
print(resp.content)
print(resp.url)
import requests

query = {'q': 'stream', 'order': 'length', 'min_width': '5000', 'min_height': '300'}
req = requests.get('https://flickr.com/en/photos/', params=query)

print(req.url)