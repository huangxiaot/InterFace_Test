# 超时处理
import requests

url = "https://tcc.taobao.com/cc/json/mobile_tel_egment.html?/tel=15059941156"
r = requests.get(url=url, timeout=2, verify=False)
print(r.text)
