import requests

url = 'http://10.220.205.251:7000/verify'
files = {'image': open('joe_test.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.json())
