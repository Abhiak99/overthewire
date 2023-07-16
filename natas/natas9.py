import re, requests
from bs4 import BeautifulSoup

username = "natas8"
password = "a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB"
url = 'http://' + username + '.natas.labs.overthewire.org'
auth = (username, password)
secret = "oubWYf2kBq"
data = {"secret": secret, "submit" : "submit"}
r = requests.post(url, auth=auth, data=data)
print(r.headers)
print(r.text)

print(re.findall(r'natas9 is (.*)', r.text))
