import urllib.request as urlb

response_url = urlb.urlopen('https://api.publicapis.org/entries')

print(response_url)

print(response_url.info())
print(response_url.read())
import urllib.request as urlb
import pprint

response_url = urlb.urlopen('https://api.publicapis.org/entries')

html = response_url.read()
pprint.pprint(html)




response_url.close()