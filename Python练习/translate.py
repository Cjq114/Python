import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入需要翻译的内容(输入“q!”退出程序)：")
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    '''
    data = {}

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client']  = 'fanyideskweb'
    data['salt'] = '15553070822704'
    data['sign'] = 'c76f722704fd0f37f126a54532553334'
    data['ts'] = '1555307082270'
    data['bv'] = '0bbb180f75b7e2f83d7b245ab1b58103'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] =  'FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode('utf-8')   #负责解析功能

    req = urllib.request.Request(url, data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' )

    response = urllib.request.urlopen(url, data)
    html = response.read()  #转换为utf-8的形式

    target = json.loads(html)
    print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))

    time.sleep(5)
