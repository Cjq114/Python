import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['1.192.242.73:9999','175.175.219.87:1133','134.119.222.248:8080','185.3.213.86:80']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
