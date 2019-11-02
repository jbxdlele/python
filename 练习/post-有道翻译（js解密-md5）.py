import random
import time
import hashlib
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '251',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1112712416.5060406; OUTFOX_SEARCH_USER_ID="-109425695@10.168.11.15"; _ga=GA1.2.41271830.1565660216; _gid=GA1.2.2009050439.1568425320; JSESSIONID=aaayvt-kWaarM5NvS330w; ___rl__test__cookies=1568613670508',
}


def get_res(i):
    # 时间戳
    ts = int(time.time() * 1000)
    # 获取随机一个数
    a = random.choice((0, 1, 3, 4, 5, 6, 7, 8, 9))
    salt = str(ts) + str(a)
    sign = f'fanyideskweb{i}{salt}n%A-rKaT5fb[Gy?;N5@Tj'
    sign = hashlib.md5(sign.encode()).hexdigest()
    bv = str(
        '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36').encode()
    bv = hashlib.md5(bv).hexdigest()

    data = {
        'i': i,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': 2.1,
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }


    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    respense = requests.post(url=url, headers=headers, data=data, )
    before = respense.json()['translateResult'][0][0]['src']
    after = respense.json()['translateResult'][0][0]['tgt']
    print(f'{before}  翻译结果是：{after}')


while True:
    i = input('请输入需要翻译的内容：')
    get_res(i)
    print('--------------------------------------------------------')

# print(respense.reason)  # 响应结果
#
# print(respense.status_code)  # 响应状态码
#
# print(respense.elapsed)  # 响应时间
#
# print(respense.request)  # 请求方式
#
# print(respense.encoding)  # 编码
#
# print(respense.apparent_encoding)  # 获取网页源码的编码
#
# print(respense.url)  # 请求url
#
# print(respense.headers)  # 响应头
#
# print(respense.request.headers)
