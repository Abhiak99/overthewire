import requests,re

username = "natas1"
password = "g9D9cREhslqBKtcA2uocGHPfMZVzeFK6"

url = "http://"+username+".natas.labs.overthewire.org"

auth = (username, password)


response = requests.get(url, auth=auth)
# print(response.text)

match = re.findall(r"<!--(.*)-->", response.text)
print(match[1])
