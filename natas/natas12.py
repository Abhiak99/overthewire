import re, requests, urllib, base64
from bs4 import BeautifulSoup

proxy = {"http": "127.0.0.1:8080"}

username = "natas11"
password = "1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg"
url = 'http://'+username+'.natas.labs.overthewire.org'
auth= (username, password)
params = {"showpassword":"yes"}

session = requests.Session()
session.cookies.update({'data':'MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz'})
r = session.get(url, auth=auth)
# print(r.headers)

# data = session.cookies['data']
# print(data)
# print(base64.b64decode(urllib.parse.unquote(data)).decode())
# print(BeautifulSoup(r.text, "html.parser").text)
print(re.findall(r'natas12 is (.*)<br>', r.text))

