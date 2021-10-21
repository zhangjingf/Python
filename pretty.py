import re
import requests
import os
from bs4 import BeautifulSoup

def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }  #模拟用户操作
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('网络状态错误')

def getUrlList(url):
    url_list = []
    demo = getHtml(url)
    soup = BeautifulSoup(demo,'html.parser')
    sp = soup.find_all('img')
    nls = re.findall(r'src=[\'\"]?([^\'\"]*)[\'\"]?', str(sp))
    for i in nls:
        if '.gif' in i:
            continue
        url_list.append(i.replace('small', '')[0:-14] + '.jpg')
    return url_list

def fillPic(url,page):
    pic_url = getUrlList(url)
    path = './file'
    for p in range(len(pic_url)):
        pic = requests.get(pic_url[p]).content
        image_name ='第{}页'.format(page) + str(p+1) + '.jpg' #给图片预定名字
        image_path = path + '/' + image_name #定义图片保存的地址
        with open(image_path, 'wb') as f: #保存图片
            f.write(pic)
            print(image_name, '下载完毕！！！')

def main():
    n = input('请输入要爬取的页数：')
    url = 'http://www.netbian.com/fengjing/'
    if not os.path.exists('./file'):
        os.mkdir('./file/')
    page = 1
    fillPic(url, page)

    if int(n) >= 2:
        ls = list(range(2, 1 + int(n)))
        url = 'http://www.netbian.com/fengjing/'
        for i in ls:
            page = str(i)
            url_page = 'http://www.netbian.com/fengjing/'
            url_page += 'index_' + page + '.htm'
            fillPic(url_page, page)
main()
