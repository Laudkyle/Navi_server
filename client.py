import requests

url = 'http://192.168.0.144:7000/verify'
try:
    with open('joe_test.jpg', 'rb') as img:
        files = {'image': img}
        response = requests.post(url, files=files, timeout=60)  
    response.raise_for_status() 
    print(response.json())
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.ConnectionError:
    print("Failed to connect to the server")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
