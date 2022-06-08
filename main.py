# 导入必要的包
from selenium import webdriver
from bs4 import BeautifulSoup
import requests




# 打开谷歌浏览器
driver = webdriver.Chrome()
# 设置要爬取的网站
driver.get('http://pic.netbian.com/4kmeinv/')
# 初始化一个引用计数，用于后面的图片简单命名
index = 1


# 定义爬虫方法
def getImage():
    # 将index置为全局变量
    global index
    # 循环爬取，循环多少次爬取多少页的图片
    for i in range(0,50):
        # 模拟点击下一页，因为爬取完一页需要点击下一页爬取
        driver.find_element_by_link_text("下一页").click()
        # 解析网页
        html = BeautifulSoup(driver.page_source, 'html.parser')
        # 获取原图的url链接
        links =html.find('div', {'class': 'slist'}).find_all('img')
        # 遍历当页获得的所有原图链接
        for link in links:

            # 将原图存至当前目录下的baidu8文件夹，以index命名，后缀名为jpg
            with open('baidu8/{}.jpg'.format(index), 'wb') as jpg:
                jpg.write(requests.get("http://pic.netbian.com/" + link.get('src')).content)

            print("正在爬取第%s张图片" % index)
            index += 1
# 定义主函数
def main():

    getImage()

main()

