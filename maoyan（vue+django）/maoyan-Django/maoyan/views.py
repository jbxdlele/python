import requests
from django.http import JsonResponse


# Create your views here.


# 正在热映
def get_movieOnInfoList(request):
    url = 'http://m.maoyan.com/ajax/movieOnInfoList?token='
    headers = {
        'Referer': 'http://m.maoyan.com',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'
    }

    res = requests.get(url, headers=headers).json()
    return JsonResponse(res)


# 即将热映
def get_comingList(request):
    url = 'http://m.maoyan.com/ajax/comingList?ci=73&token=&limit=10'
    headers = {
        'Referer': 'http://m.maoyan.com',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'
    }

    res = requests.get(url, headers=headers).json()
    return JsonResponse(res)


# 获取影城信息
def get_cinemaList(request):
    url = 'http://m.maoyan.com/ajax/cinemaList?day=2019-10-31&offset=0&limit=20&districtId=-1&lineId=-1&hallType=-1&brandId=-1&serviceId=-1&areaId=-1&stationId=-1&item=&updateShowDay=true&reqId=1572519440844&cityId=73'
    headers = {
        'Referer': 'http://m.maoyan.com',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'
    }

    res = requests.get(url, headers=headers).json()
    return JsonResponse(res)

# print(get_movieOnInfoList())
#
# print('*'*100)
# print(get_comingList())
# print('*'*100)
# print(get_cinemaList())
