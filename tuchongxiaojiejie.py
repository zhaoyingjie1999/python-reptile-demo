'用爬虫获取图虫网小姐姐图片'

import requests
import time
from PIL import Image
from io import BytesIO

# def saveImg(url, name):
#     data = requests.get(url, headers=header)
#     img = Image.open(BytesIO(data.content))
#     etc = '.jpg'
#     if img.mode == 'RGBA':
#         etc = '.png'
#     if img.mode != 'RGBA' and img.mode != 'RGB':
#         img = img.convert('RGBA')
#         etc = '.png'
#     fileName = name + etc
#     img.save('./shaonvxiaojiejie/%s' % fileName)
#     print('下载 %s 完成' % fileName)
#     img.close()
#     return

# tag = input('要爬取的类型: ')
# num = input('要爬取几条数据: ')
# page = input('要爬取第几页数据: ')
# dataList = requests.get('https://tuchong.com/rest/tags/%s/posts?page=%s&count=%s&order=weekly' % (tag, page, num), headers = header, allow_redirects = False)
# jsonList = dataList.json()

# print('爬取完成, 开始解析图片')
# i = 0
# for item in jsonList['postList']:
#     i += 1
#     print('---------------------------------------------------解析第%s条数据---------------------------------------------------' % i)
#     if item['type'] == 'multi-photo':
#         print('这条数据的类型是 multi-photo')
#         t = 0
#         for img in item['images']:
#             t += 1
#             print('解析第%s张图片中' % t, '1', item['site_id'], '2', img['img_id'])
#             saveImg('https://photo.tuchong.com/%s/f/%s.jpg' % (item['site_id'], img['img_id']), '%s-%s.jpg' % (item['site_id'], img['img_id']))
#     else:
#         print('这条数据的类型是 text', '1', item['post_id'], '2', item['site_id'])
#         saveImg(item['title_image']['url'], '%s-%s.jpg' % (item['post_id'], item['site_id']))
#     time.sleep(0.5)

class Fetch:
    def __init__(self, header):
        self.header = header
        self.tag = input('要爬取的类型: ')
        self.num = input('要爬取几条数据: ')
        self.page = input('要爬取第几页数据: ')
        self.parse(self.request())
    def request(self):
        data = requests.get('https://tuchong.com/rest/tags/%s/posts?page=%s&count=%s&order=weekly' % (self.tag, self.page, self.num), headers = self.header, allow_redirects = False)
        return data.json()
    def parse(self, jsonList):
        i = 0
        for item in jsonList['postList']:
            i += 1
            print('---------------------------------------------------解析第%s条数据---------------------------------------------------' % i)
            if item['type'] == 'multi-photo':
                print('这条数据的类型是 multi-photo')
                t = 0
                for img in item['images']:
                    t += 1
                    print('解析第%s张图片中' % t)
                    DownloadImg('https://photo.tuchong.com/%s/f/%s.jpg' % (item['site_id'], img['img_id']), './ceshi/%s-%s.jpg' % (item['site_id'], img['img_id']), self.header)
            else:
                print('这条数据的类型是 text')
                DownloadImg(item['title_image']['url'], './ceshi/%s-%s.jpg' % (item['post_id'], item['site_id']), self.header)
            time.sleep(0.5)



class DownloadImg:
    def __init__(self, url, name, header):
        data = requests.get(url, headers=header)
        img = Image.open(BytesIO(data.content))
        self.fileName = self.checkFileName(name, img)
        img.save(self.fileName)
        img.close()
    def getName(self):
        return self.fileName
    def checkFileName(self, name, img):
        etc = '.jpg'
        if img.mode == 'RGBA':
            etc = '.png'
        if img.mode != 'RGBA' and img.mode != 'RGB':
            img = img.convert('RGBA')
            etc = '.png'
        return name + etc


header = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

Fetch(header)
