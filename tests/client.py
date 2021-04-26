import requests

raw = input('enter args: ')
args = raw.split(" ")
url = ""

for i in range(len(args)):
    url += args[i]
    if i < len(args) - 1:
        url += "_"

r = requests.get("http://127.0.0.1:5000/" + url)
print(r.text)
