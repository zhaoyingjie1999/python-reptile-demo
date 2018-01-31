'指定url下载视频'

import requests
from progress.bar import ShadyBar
import time

url = 'http://dl164.80s.im:920/1801/伏地魔：传人的起源/伏地魔：传人的起源_bd.mp4'
url1 = 'http://newoss.maiziedu.com/machinelearning/pythonrm/pythonrm5.mp4'
url2 = 'http://dl163.80s.im:920/1801/雷神3：诸神黄昏/雷神3：诸神黄昏_bd.mp4'
url3 = 'ftp://m:m@tv.kaida365.com:2199/神盾局特工第五季06.mp4'
reNum = 0
name = time.time()

def download(url, name):
    print('download %s start' % name)
    # try:
    res = requests.get(url, stream=True)
    size = int(res.headers['content-length'])
    chunk_size = 2048
    nowSize = 0
    start_time = int(time.time())
    print('总长度为 %sKB, %sMB' % (size /1024, size / 1024 / 1024))
    # bar = ShadyBar(name, max=100, suffix='%(percent)d%%')
    with open(name, 'wb') as f:
        for chunk in res.iter_content(chunk_size):
            f.write(chunk)
            nowSize += chunk_size
            # print(size, '----', nowSize, '----', int(nowSize / size * 100))
            # bar.next(int(nowSize / size * 100))
        # bar.finish()
    end_time = int(time.time())
    # print('下载完成 文件总大小%sMB 用时%s秒 平均每秒下载%sMB' % (size / 1024 / 1024, end_time - start_time, (size / 1024 / 1024) / (end_time - start_time)))
    # except e as identifier:
        # if reNum < 5:
            # print('error, re download')
            # download(url, name)
        # else:
            # print('error number more than five times, exit')

def downloadVideoList(video):
    for v in video['list']:
        print('开始下载')
        file_name = video['path'] + '/' + v['name'] + '.' + v['type']
        download(v['url'], file_name)
        print('下载完成')


if __name__ == '__main__':
    download(url1, './%s.mp4' % int(name))
    # video = {
    #     'path': './down',
    #     'list': [
    #         {
    #             'url': 'http://newoss.maiziedu.com/machinelearning/pythonrm/pythonrm5.mp4',
    #             'name': 'hhd',
    #             'type': 'mp4'
    #         },
    #         {
    #             'url': 'http://dl163.80s.im:920/1801/雷神3：诸神黄昏/雷神3：诸神黄昏_bd.mp4',
    #             'name': '雷神3',
    #             'type': 'mp4'
    #         }
    #     ]
    # }
    # # downloadVideoList(video)
    # aa = input('下第几个')
    # if aa == '1':
    #     download(url, './down/aaa.mp4')
    # else:
    #     download(url2, './down/bbb.mp4')
