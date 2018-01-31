'解析html'

# 扒的是慕课网JavaScript分类下的 https://www.imooc.com/course/list?c=javascript
# 因为是练习解析html, 所以不涉及分页

# 请求库
import requests
# 解析html的库 安装 pip install lxml
from lxml import etree

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
for page in range(1, 5):
    data = requests.get('https://www.imooc.com/course/list?c=javascript&page=%s' % page, headers = headers)
    print('爬取完成, 开始解析')
    print('---------------')
    html = etree.HTML(str(data.content, encoding = "utf-8"))
    # 第一种方法 cssselect 这个需要安装 pip install cssselect
    # 获取课程卡片 返回一个list
    card = html.cssselect('.course-card-container')
    print('使用cssselect解析')
    for index, car in enumerate(card):
        print('解析第%s个课程' % index)
        class_link = car.cssselect('.course-card')[0]
        one_class = car.cssselect('.course-card-name')[0]
        # 获取课程名称 返回的是一个list 取第一个 也是唯一的一个
        print('课程名称: ', one_class.text)
        # 获取class attrib 是一个字典
        print(one_class.attrib['class'])
        print('课程地址: ', 'https://www.imooc.com%s' % class_link.attrib['href'])
        print('---------------')

    # 第二种方法 xpath 这个lxml自带的
    # xpath 是从html开始寻找的
    # cardr = html.xpath('/html/body/div[@id="main"]/div[@class="container"]/div[@class="course-list"]/div[@class="moco-course-list"]/ul[@class="clearfix"]/div[@class="course-card-container"]')
    # print('使用cssselect解析')
    # # xpath 的语法简单, 但是比较繁琐
    # for index, car in enumerate(cardr):
    #     print('解析第%s个课程' % index)
    #     class_link = car.xpath('./a[@class="course-card"]')[0]
    #     # 获取课程名称和class名 . 说明在当前的元素
    #     one_class = car.xpath('./a[@class="course-card"]/div[@class="course-card-content"]/h3[@class="course-card-name"]')[0]
    #     print('课程名称: ', one_class.text)
    #     print(one_class.attrib['class'])
    #     print('课程地址: ', 'https://www.imooc.com%s' % class_link.attrib['href'])
    #     print('---------------')