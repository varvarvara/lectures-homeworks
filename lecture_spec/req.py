import json

import requests
url = "https://ria.ru/20251016/mid-2048557368.html"
res = requests.get(url)

print(res)