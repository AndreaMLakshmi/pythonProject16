import requests
response = requests.get(url='http://127.0.0.1:8000/our_endpoints/server_time')
print(response.text)
files = {'text':('test.txt', open('test.txt', 'rb'))}
print(response.status_code)
response = requests.head("http://127.0.0.1:8000/our_endpoints/status2/")
print(response.status_code)
payload = '{"record": "NEW_RECORD"}'
response = requests.put("http://127.0.0.1:8000/our_endpoints/save_json_to_file/",data=payload)
print(response.status_code)
file_to_delete = '{"file_name":"test01"}'
response = requests.delete(url='http://127.0.0.1:8000/our_endpoints/delete_file/', data=file_to_delete)
print(response.status_code)
patch_data = '{"updates":"Some new Stuff"}'
response = requests.patch(url='http://127.0.0.1:8000/our_endpoints/update_file/', data=patch_data)
print(response.status_code)

files = {'text':('test.txt', open('test.txt', 'rb'))}
response = requests.post(url='http://127.0.0.1:8000/our_endpoints/upload_file/', files=files)

print("STATUS CODE: ", response.status_code)
print("CONTENT: ", response.content)
