import requests
urls = {'google': 'https://www.google.com', 'httpbin': {'url': 'https://httpbin.org', 'uri': ('get', 'response-headers', 'post')}}
class PostRequest:
    @classmethod
    def make_post_request(self, url, data=None, headers=None):
        return requests.post(url=url, data=data, headers=headers)
    @classmethod
    def print_response_headers(self, response_headers):
        for key, value in response_headers.items():
            print(key, ": ", value)


pr = PostRequest()

headers_post = {'User-Agent': 'My User Agent 1.0'}
data = {'Something': 'Anything'}

resp = pr.make_post_request(url=urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][2], data=data, headers=headers_post)

print(pr.print_response_headers(resp.headers))
print("STATUS_CODE: ", resp.status_code)
print(resp.text)
print(resp.url)