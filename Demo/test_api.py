import requests

r = requests.get(url="https://baidu.com")
# 打印返回的正文信息
print(r.text)
# 返回的编码方式
print(r.encoding)
# url地址
print(r.url)
#返回的消息头
print(r.headers)
# 返回的用户辨明信息，cookies
print(r.cookies)
# 返回的正文信息，用二进制去保存
print(r.content)
