import time,random

from bs4 import BeautifulSoup

from selenium import webdriver
# chrome_driver=r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"

job="前端"
page=3
htmls_list =[]
for num in range(1,page,1):
    url = "https://www.zhipin.com/c101010100/?query={}&page=1&ka=page-{}".format(job,num)
    driver=webdriver.Chrome()   #初始化webdriver executable_path=chrome_driver
    driver.get(url)  #自动化运行页面
    time.sleep(5);
    htmls=driver.page_source #获取页面信息
    htmls_list.append(str(htmls)) #将获取页面信息添加至网页存储列表
    driver.close() #关闭浏览器
    ran_time = random.randint(1,5) #随机生成停顿时间
    time.sleep(ran_time) #程序休眠

info_list=[]   #建立获取职位信息存储列表
for htmls in htmls_list:
    soup= BeautifulSoup(htmls) #解析网页
for i in soup.find_all("div", class_="job-primary"):
        job = i.find_all("a")  #获取招聘岗位信息
        area = i.find_all('span', class_='job-area') #获取工作地点 
        salary = i.find_all('span', class_='red') #获取薪酬信息
        title = i.find_all("h3")[1].get_text() #获取企业名称
        industry = i.find_all('a',class_="false-link")[0].get_text() #获取所属行业
        edu = i.find_all('p')[0].text  #获取学历要求
        scale = i.find_all('p')[1].text #获取条件信息
        url = "https://www.zhipin.com/" + i.find_all("div", class_="primary-box")[0]['href'] #获取详情页信息
        info_list.append([title, industry, job[0]['title'],area[0].get_text(),edu,scale, salary[0].get_text(),url])#将所有信息保存至列
print(info_list)