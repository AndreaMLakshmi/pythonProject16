import requests
r = requests.head('https://jsonplaceholder.typicode.com/posts/1')
print(r.headers)
url = 'https://jsonplaceholder.typicode.com/posts/1'
myobj = {
    'title': 'Inserted through requests library',
    'body': 'This post was inserted through the requests library in Python. This was performed using a PUT request',
    'userId': 1,
    'id':1
}
x = requests.put(url, data = myobj)
print(x.text)
r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)