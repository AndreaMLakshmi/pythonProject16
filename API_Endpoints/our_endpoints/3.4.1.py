import json
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
print(type(r.text))

content = json.loads(r.text)
print(content['title'])
print(type(content))
data = '{"name":"joe", "lastname":"Doe", "age":18}'
data_parsed = json.loads(data)
print(type(data))
print(type(data_parsed))
print(data_parsed['lastname'])
sample_data_01 = { "name": "John", "lastname": "Doe", "age": 24}
sample_data_01_json = json.dumps(sample_data_01)
print(type(sample_data_01_json))
print(sample_data_01_json)
sample_data_02 = {
  "name": "John",
  "age": 24,
  "married": True,
  "divorced": False,
  "children": ("Bruce"),
  "cars": [
    {"model": "corolla", "year": 2020},
  ]
}

print(json.dumps(sample_data_02))
print(json.dumps(sample_data_02, indent=4))
print(json.dumps(sample_data_02, indent=4, separators=(". ", " = ")))