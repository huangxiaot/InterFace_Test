# https证书
import tempfile

import requests

url = "https://www.ctrip.com/"
# 1、忽略证书
r = requests.get(url=url, verify=False)     #verify参数默认为true，false表示忽略证书
print(r.text)

# 2、添加证书的路径
r = requests.get(url=url, verify="证书的路径")
print(r.text)
