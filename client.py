import requests

url = 'http://192.168.0.144:7000/verify'
files = {'image': open('joe_test.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.json())
