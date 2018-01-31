'用爬虫获取淘女郎小姐姐的图片和名字'

import requests
import time
from PIL import Image
from io import BytesIO

def saveImg(url, name):
    data = requests.get(url, headers = header)
    img = Image.open(BytesIO(data.content))
    etc = '.jpg'
    if img.mode == 'RGBA':
        etc = '.png'
    if img.mode != 'RGBA' and img.mode != 'RGB':
        img = img.convert('RGBA')
        etc='.png'
    fileName = name + etc
    img.save('./taonvlang/%s' % fileName)
    print('下载 %s 完成' % fileName)
    img.close()
    return

header = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

for i in range(1, 68):
    dataList = requests.get('https://mm.taobao.com/alive/list.do?scene=all&page=%s' % i, headers = header, allow_redirects = False)
    jsonList = dataList.json()

    print('--------------------爬取第%s页完成, 开始解析图片--------------------' % i)
    for item in jsonList['dataList']:
        url = item['avatarUrl']
        if not ('http' in item['avatarUrl'] or 'https' in item['avatarUrl']):
            url = 'http:%s' % item['avatarUrl']
        saveImg(url, '%s-%s' % (item['darenNick'], item['userId']))
    time.sleep(1)
