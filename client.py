import requests

url = 'http://10.206.35.46:80/verify'
files = {'image': open('joe_test.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.json())
