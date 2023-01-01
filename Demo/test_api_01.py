import requests

url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%25B8%25B8%25E6%2588%258F%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
r_51job = requests.get(url=url)
print(r_51job.text)
print(r_51job.encoding)
r_51job.encoding = 'gb2312'
print(r_51job.text)
