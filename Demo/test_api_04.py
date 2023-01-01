# auth鉴权，发生接口请求时，添加auth鉴权
import requests

url = "http://106.12.126.197:3000/"
# 参数auth=("用户名"，"密码")
r = requests.get(url=url, auth=("cxy001", "123456"))
print(r.text)
