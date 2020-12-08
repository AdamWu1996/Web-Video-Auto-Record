
import json
import time
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from python3_anticaptcha import ImageToTextTask

# ============================ for selenium ============================ 
option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=option)
    
def getDuartions():
    url = "https://cek.ott2b.hinet.net/learning/dist/#/home"
    driver.get(url)
    
    input('Login Btn')
    # 登入按鈕
    login = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/header/div/div[6]/button[1]")
    login.click()
    
    driver.implicitly_wait(1)
    account = driver.find_element_by_id('input-93')
    account.send_keys('P223502682')
    pwd = driver.find_element_by_id('input-97')
    pwd.send_keys('cross910188')
    input('等待展開課程')
    duartions = driver.find_elements_by_class_name("duration")
    return duartions

def duartionTransfer(duartions):
    def textToNum(text):
        for idx,i in enumerate(text):
            try:
                text[idx] = int(i.lstrip("0"))
            except:
                text[idx] = 0
        if idx == 1:
            text.insert(0,0)
        return text
            
    duartion_list = []
    for duartion in duartions:
        x = textToNum(duartion.text.split(":"))
        duartion_list.append(x)
    return duartion_list


duartions = getDuartions()
duartions = duartionTransfer(duartions)
print(duartions)

# ============================ 動態爬蟲 ============================ 
# 誠誠 : https://youtu.be/IMOUf4BYTG8

# XHR Header 裡的 Url
Request_URL = str(input('Api url : '))
Autho = str(input('認證 : '))

# 網站需要驗證 authorization
request = req.Request(Request_URL, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4280.66 Safari/537.36'
                                   ,'authorization': Autho})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")


data = json.loads(data)
courses = data['courses']

course_code = []
lesson_code = []
idx = 0

for idx,course in enumerate(courses):
    course_code.append(course['hid'])
    lesson_code.append([])
    for lesson in course['lessons']:
        lesson_code[idx].append(lesson['hid'])

# lesson_code.reverse()
# course_code.reverse()

def print_course(course_code):
    print('\t\t\t{')
    for i,course_ in enumerate(course_code):
        print('\t\t\t\t\'ch' + str(i+1) + '\':\'' + course_ + '\',')
    print('\t\t\t},')
    
def print_lesson(lesson_code):
    for i,course in enumerate(lesson_code):
        print('\t\t\t{')
        for j,lesson in enumerate(course):
            print('\t\t\t\t\'l' + str(i+1)+'-'+str(j+1)+'\':\'' + lesson + '\',')
        print('\t\t\t},')

def print_recorded(lesson_code):
    for i,course in enumerate(lesson_code):
        print('\t\t\t{')
        for j,lesson in enumerate(course):
            print('\t\t\t\t\'l' + str(i+1)+'-'+str(j+1)+'\':False,')
        print('\t\t\t},')        

# 把時間依照 lesson 排好
def print_time(duartions,lesson_code):
    tmp = []
    index = 0
    for idx, lesson in enumerate(lesson_code):
        tmp.append([])
        for _ in lesson:
            tmp[idx].append(duartions[index])
            index = index + 1
    for i in tmp:
        print(i,',')

print_course(course_code)        
print_lesson(lesson_code)
print_recorded(lesson_code) 
print_time(duartions, lesson_code)
