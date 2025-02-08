import requests

server = input().strip()
port = int(input())
a = int(input())
b = int(input())

url = f"{server}:{port}"
params = {'a': a, 'b': b}

response = requests.get(url, params=params)
data = response.json()

sorted_result = sorted(data['result'])
print(' '.join(map(str, sorted_result)))
print(data['check'])
