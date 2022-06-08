# encoding:utf-8
import requests
import re
from bs4 import BeautifulSoup

header = {"Referer": "http://", "User-agent": "Mozilla/5.0"}  # 输入和imagepage类似的网址


# 1-1000
def getImg(img_url, img_name):
    jpg_url = img_url
    r = requests.get(jpg_url, headers=header)

    if r.status_code == 200:
        print
        img_url + "   success"
    content = r.content
    with open(img_name, 'wb') as fp:
        fp.write(content)


# 获得专辑照片数量
def picSetNum(picSet_url):
    r_set = requests.get(picSet_url, headers=header)
    html_set = r_set.content
    soup_set = BeautifulSoup(html_set, 'html.parser')
    tag_pagename = soup_set.find_all(href=re.compile('^/mm/'))
    return tag_pagename[0].string


if __name__ == '__main__':
    homepage = "http://pic.netbian.com/4kmeinv/"  # 输入你要爬取的目标地址
    imgpage = "D:/YOU"  # 输入图片的存储位置
    for i in range(1, 3):
        temp_url = homepage + str(i)
        for j in range(1, int(picSetNum(temp_url)) + 1):
            t_url = imgpage + str(i) + '/' + str(j) + '.jpg'
            t_name = 'mm_' + str(i) + '_' + str(j) + '.jpg'
            print (t_url)
            # print t_name
            getImg(t_url, t_name)
