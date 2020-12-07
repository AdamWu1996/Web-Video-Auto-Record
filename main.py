import pyperclip, pyautogui, os, shutil
import time as T
import cv2 as cv
import numpy as np

def click():
    try:
        pyautogui.click()
    except:
        pass


def getUrl(course, lesson, idx):
    COURSE_CODE = {
				'ch1':'mlmdznKb',
				'ch2':'xX4PdaXO',
				'ch3':'YXexLBqM',
				'ch4':'YK7BzrXk',
				'ch5':'VXwwL5XJ',
				'ch6':'zXxwLgq9',
				'ch7':'YX5BGGK2',
				'ch8':'yKgE34qn',
				'ch9':'JXO6nAqV',
				'ch10':'8lnZLzl7',
				'ch11':'pq0GzQlD',
				'ch12':'Jqy6DjXL',
				'ch13':'jlM3yJXe',
				'ch14':'Vqo7LpqZ',
				'ch15':'PKjeLvXw',
				'ch16':'Aq1az5qn',
				'ch17':'GlAazWle',
				'ch18':'NlRr5Jlw',
				'ch19':'zKVWe7lD',
				'ch20':'MXNe0BqY',
				'ch21':'9lp3L7K7',
				'ch22':'bl9BzVq4',
				'ch23':'NKaZL5lm',
				'ch24':'2KBWzplp',
				'ch25':'rl8BPvXV',
                'ch26':'bKbJLaK4',
				'ch27':'nXvwL0KY',
				'ch28':'WXWg4oXv',
				'ch29':'OKQMg3KZ',
				'ch30':'jKZWBvlz',
                'ch31':'VlJmOnKo',
			}

    LESSON_CODE = [
            {
				'l1-1':'al6Qd1Kr',
				'l1-2':'pq0oVylD',
				'l1-3':'8lnDgjX7',
				'l1-4':'JXORQVqV',
				'l1-5':'yKgQO7qn'
			},
			{
				'l2-1':'OKQPRzXZ',
                'l2-2':'VXwMxRlJ',
				'l2-3':'YX5ONal2',
				'l2-4':'YK75R8qk',
				'l2-5':'zXxydwK9'
			},
			{
				'l3-1':'2KBPdeqp'
			},
			{
				'l4-1':'Yq2apnlN',
				'l4-2':'al6gV9qr',
				'l4-3':'Yq2yoOlN',
				'l4-4':'rlLEk1qg',
				'l4-5':'GKzn38Kz'
			},
			{
				'l5-1':'jKZPO5qz',
				'l5-2':'VlJL3nXo',
				'l5-3':'jKd9OPlp',
				'l5-4':'pKGbegXr',
				'l5-5':'eqPAQOXB'
			},
			{
				'l6-1':'nXvG7aKY',
				'l6-2':'GlA9ZZle'
			},
			{
				'l7-1':'9lpGnGK7',
				'l7-2':'kXDQbLK8',
				'l7-3':'1lEWQAXP',
				'l7-4':'MXNVQPXY',
				'l7-5':'zKV0k0qD'
			},
			{
				'l8-1':'bl9bdpq4',
				'l8-2':'NlRjdDlw',
				'l8-3':'GlA9y0le',
				'l8-4':'Aq1Mjbqn',
				'l8-5':'PKjb8jKw'
			},
			{
				'l9-1':'rlLPd0lg',
				'l9-2':'kXDQ6aK8',
				'l9-3':'1lEW6gXP',
				'l9-4':'MXNVr9XY',
				'l9-5':'zKV09yqD'
			},
			{
				'l10-1':'al6Y0OKr',
				'l10-2':'Yq2Yb1lN',
				'l10-3':'rlLgAOKg',
				'l10-4':'GKzzgyKz',
				'l10-5':'NKaG4Aqm'
			},
			{
				'l11-1':'OKQeorKZ',
				'l11-2':'WXWEeDlv',
				'l11-3':'nXvz9dXY',
				'l11-4':'bKbn9oK4',
				'l11-5':'bKbPmGq4'
			},
			{
				'l12-1':'NKa0nZXm',
				'l12-2':'bl9YgNl4',
				'l12-3':'9lpzZEX7',
				'l12-4':'jKZR8aKz',
				'l12-5':'WXWky2Xv'
			},
			{
				'l13-1':'xX4Y00KO',
				'l13-2':'mlmBjJqb',
				'l13-3':'rl8Y8OqV',
				'l13-4':'2KBRm2Kp',
				'l13-5':'GKzG8Wlz'
			},
			{
				'l14-1':'zXx496X9',
				'l14-2':'VXweBklJ',
				'l14-3':'YK7Ga6Kk',
				'l14-4':'YXeEvvXM',
				'l14-5':'VlJPnVXo'
			},
			{
				'l15-1':'8lnyAQK7',
				'l15-2':'JXONW9qV',
				'l15-3':'yKgVLMXn',
				'l15-4':'YX5p46q2',
				'l15-5':'jKdGgaXp'
			},
			{
				'l16-1':'Vqo0jeXZ',
				'l16-2':'jlMD9OKe',
				'l16-3':'JqymZGqL',
				'l16-4':'pq0QyoXD',
				'l16-5':'pKGPM6lr'
			},
			{
				'l17-1':'NlRAzbKw',
				'l17-2':'GlAdEJKe',
				'l17-3':'Aq1rndXn',
				'l17-4':'PKj1kQXw',
				'l17-5':'eqPP7jqB'
			},
			{
				'l18-1':'kXDdj1X8',
				'l18-2':'1lEdM4KP',
				'l18-3':'MXNEZmqY',
				'l18-4':'zKVMDeXD',
				'l18-5':'8qkGm4qd'
			},
			{
				'l19-1':'xXrgODKa',
				'l19-2':'Gl3pxpqd',
				'l19-3':'dlYPVoKy'
			},
			{
				'l20-1':'jlMyZ1le',
				'l20-2':'JqyD5olL',
				'l20-3':'xXrGYVKa'
			},
            {
				'l21-1':'Gl39YMXd',
				'l21-2':'GKznYnKz',
				'l21-3':'VlJLOQXo',
				'l21-4':'jKd9YMlp',
				'l21-5':'pKGbQ5Xr'
			},
			{
				'l22-1':'kXDP13X8',
				'l22-2':'eqPAn4XB',
				'l22-3':'8qk6peld',
				'l22-4':'dlYg6yXy',
				'l22-5':'xXrRajXa'
			},
			{
				'l23-1':'1lEPjQKP',
				'l23-2':'Gl303xqd',
				'l23-3':'kXDQGaK8',
				'l23-4':'1lEWGgXP',
				'l23-5':'MXNVd9XY'
			},
			{
				'l24-1':'VqozMVlZ',
				'l24-2':'jlM5xxle',
				'l24-3':'Jqyz1OXL',
				'l24-4':'pq0YAjXD',
				'l24-5':'MXNPxrlY'
			},
			{
				'l25-1':'NlR41LXw',
				'l25-2':'GlAV1Zqe',
				'l25-3':'Aq1YGpqn',
				'l25-4':'PKj4xkqw',
				'l25-5':'NlRP4NXw'
			},
            {
				'l26-1':'8qkm85Kd',
				'l26-2':'dlYV49qy',
				'l26-3':'xXrY1Gqa',
				'l26-4':'Gl3Yo0Xd',
				'l26-5':'zKVP3rqD'
			},
			{
				'l27-1':'VlJn5alo',
				'l27-2':'jKdgarXp',
				'l27-3':'pKGMD3qr',
				'l27-4':'eqP7RNlB',
				'l27-5':'GlAPVpKe'
			},
			{
				'l28-1':'Aq1BY4Xn',
				'l28-2':'zKV0ryqD',
				'l28-3':'NlRjmrlw',
				'l28-4':'GlA94mle',
				'l28-5':'Aq1MWoqn'
			},
			{
				'l29-1':'OKQeWnKZ',
				'l29-2':'WXWE1Ylv',
				'l29-3':'nXvz2RXY',
				'l29-4':'bKbnQmK4',
				'l29-5':'PKjG42lw'
			},
			{
				'l30-1':'NKa0pJXm',
				'l30-2':'bl9Yral4',
				'l30-3':'9lpzRQX7',
				'l30-4':'jKZRw6Kz',
				'l30-5':'VqoGzOqZ'
			},
         {
				'l31-1':'rl8PQ2lV',
				'l31-2':'2KBzLVKp',
				'l31-3':'NKaLDnXm'
			},
    ]
    
    url = 'https://cek.ott2b.hinet.net/learning/dist/#/course/' + COURSE_CODE.get(course) + '/learn/' + LESSON_CODE[idx].get(lesson)
    return url

def goUrl(coordinate, url):
    pyautogui.moveTo(coordinate[0], coordinate[1])
    click()
    pyperclip.copy(url)
    pyperclip.paste()
    pyautogui.hotkey('ctrl', 'v', interval = 0.15)
    pyautogui.press('enter')

def waitTime(h, m, s):
    print('wait for ' + str(h) + ':' + str(m) + ':' + str(s))
    return T.sleep( (3600*h + 60*m + s)/2 )

def record(time, course, lesson, path, idx):
    print('starting...')
    pyautogui.press('f2')
    waitTime(0, 0, 5)
    x2Play()
    waitTime(0, 0, 3)
    autoPlay()
    waitTime(0, 0, 3)
    x2Play()
    waitTime(0, 0, 3)
    waitTime(time[0], time[1], time[2])
    print('ending')
    waitTime(0, 0, 3)
    pyautogui.press('f2')
    waitTime(0, 0, 3)
    _, _, files = os.walk(path).__next__()
    _, extension = os.path.splitext(files[idx])
    file_path = path + '\\' + files[idx]
    dest_path = path + '\\' + lesson + '(2x)' + extension
    os.rename(file_path, dest_path)

def autoPlay():
    img_rgb = pyautogui.screenshot()
    img_rgb = cv.cvtColor(np.array(img_rgb), cv.COLOR_RGB2BGR) 
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    play_icon = cv.imread('Play.png',0)
    w, h = play_icon.shape[::-1]
    result = cv.matchTemplate(img_gray,play_icon,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( result >= threshold)
    if( loc[0].size > 0 ):
        pyautogui.moveTo(loc[1][0],loc[0][0])
        click()

def packVideo(course, path, new_folder_path):
    _, _, files = os.walk(path).__next__()
    for file in files:
        shutil.move(path + '\\' + file, new_folder_path)
        
    
# def x2Play():
#     pyautogui.moveTo(1180,837)
#     waitTime(0, 0, 1)
#     pyautogui.moveTo(1184,685)
#     click()
#     pyautogui.moveTo(1386,1063)
#     click()
#     waitTime(0, 0, 1)

def x2Play():
    img_rgb = pyautogui.screenshot()
    img_rgb = cv.cvtColor(np.array(img_rgb), cv.COLOR_RGB2BGR) 
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    play_icon = cv.imread('1x.png',0)
    w, h = play_icon.shape[::-1]
    result = cv.matchTemplate(img_gray,play_icon,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( result >= threshold)
    if( loc[0].size > 0 ):
        pyautogui.moveTo(loc[1][0],loc[0][0])
        for i in range(4):
            T.sleep(0.5)
            click()
        pyautogui.moveTo(1386,1063)

# URL_COR = [1505, 51]
URL_COR = [1302, 61]
RECORDED = [
			       {
				'l1-1':True,
				'l1-2':True,
				'l1-3':True,
                'l1-4':True,
                'l1-5':True,
			},
			{
				'l2-1':True,
				'l2-2':True,
				'l2-3':True,
				'l2-4':True,
				'l2-5':True
			},
			{
				'l3-1':True
			},
			{
				'l4-1':True,
				'l4-2':True,
				'l4-3':True,
				'l4-4':True,
				'l4-5':True
			},
			{
				'l5-1':True,
				'l5-2':True,
				'l5-3':True,
				'l5-4':True,
				'l5-5':True
			},
			{
				'l6-1':True,
				'l6-2':True
			},
			{
				'l7-1':True,
				'l7-2':True,
				'l7-3':True,
				'l7-4':True,
				'l7-5':True
			},
			{
				'l8-1':True,
				'l8-2':True,
				'l8-3':True,
				'l8-4':True,
				'l8-5':True
			},
			{
				'l9-1':True,
				'l9-2':True,
				'l9-3':True,
				'l9-4':True,
				'l9-5':True
			},
			{
				'l10-1':True,
				'l10-2':True,
				'l10-3':True,
				'l10-4':True,
				'l10-5':True
			},
			{
				'l11-1':True,
				'l11-2':True,
				'l11-3':True,
				'l11-4':True,
				'l11-5':True
			},
			{
				'l12-1':True,
				'l12-2':True,
				'l12-3':True,
				'l12-4':True,
				'l12-5':True
			},
			{
				'l13-1':True,
				'l13-2':True,
				'l13-3':True,
				'l13-4':True,
				'l13-5':True
			},
			{
				'l14-1':True,
            'l14-2':True,
            'l14-3':True,
            'l14-4':True,
            'l14-5':True
                
			},
			{
				'l15-1':True,
				'l15-2':True,
				'l15-3':True,
				'l15-4':True,
				'l15-5':True
			},
			{
				'l16-1':True,
				'l16-2':True,
				'l16-3':True,
				'l16-4':True,
				'l16-5':True
			},
			{
				'l17-1':True,
				'l17-2':True,
            'l17-3':True,
            'l17-4':True,
            'l17-5':True
			},
			{
				'l18-1':True,
				'l18-2':True,
				'l18-3':True,
				'l18-4':True,
				'l18-5':True
			},
			{
				'l19-1':True,
				'l19-2':True,
				'l19-3':True
			},
			{
				'l20-1':True,
				'l20-2':True,
				'l20-3':True
			},
			{
				'l21-1':True,
				'l21-2':True,
				'l21-3':True,
				'l21-4':True,
				'l21-5':True
			},
			{
				'l22-1':True,
				'l22-2':True,
				'l22-3':True,
				'l22-4':True,
				'l22-5':True
			},
			{
				'l23-1':True,
				'l23-2':True,
				'l23-3':True,
				'l23-4':True,
				'l23-5':True
			},
			{
				'l24-1':True,
				'l24-2':True,
				'l24-3':True,
				'l24-4':True,
				'l24-5':True
			},
			{
				'l25-1':True,
				'l25-2':True,
				'l25-3':True,
				'l25-4':True,
				'l25-5':True
			},
			{
				'l26-1':True,
				'l26-2':True,
				'l26-3':True,
				'l26-4':True,
				'l26-5':True
			},
			{
				'l27-1':True,
				'l27-2':True,
				'l27-3':True,
				'l27-4':True,
				'l27-5':True
			},
			{
				'l28-1':True,
				'l28-2':True,
				'l28-3':True,
				'l28-4':True,
				'l28-5':True
			},
			{
				'l29-1':True,
				'l29-2':True,
				'l29-3':True,
				'l29-4':False,
				'l29-5':False
			},
			{
				'l30-1':False,
				'l30-2':False,
				'l30-3':False,
                'l30-4':False,
                'l30-5':False
			},
			{
				'l31-1':False,
				'l31-2':False,
				'l31-3':False
			}
    ]

LESSON_TIME = [ [[2, 41, 25], [0, 51, 29], [0, 28, 17], [0, 50, 25],[0, 31, 14]] ,
[[2, 44, 25], [0, 50, 15], [0, 32, 26],[0, 53, 9], [0, 28, 35] ] ,
[[2, 41, 15]] ,
[[2, 45, 56], [0, 51, 23], [0, 43, 29], [0, 52, 20], [0, 18, 44]] ,
[[2, 43, 14], [0, 50, 0], [0, 47, 22], [0, 50, 35], [0, 15, 16]],
[[2, 44, 44], [2, 44, 44]],
[[2, 36, 25], [0, 50, 25], [0, 36, 12], [0, 50, 24], [0, 19, 24]] ,
[[2, 46, 2], [0, 51, 47], [0, 50, 55], [0, 50, 17], [0, 13, 3]] ,
[[2, 48, 6], [0, 50, 58], [0, 49, 59], [0, 52, 33], [0, 14, 36]] ,
[[0, 50, 15], [0, 47, 40], [0, 50, 49], [0, 14, 36], [2, 43, 20]] ,
[[0, 52, 14], [0, 32, 26], [0, 50, 42], [0, 25, 20], [2, 40, 42]] ,
[[0, 51, 47], [0, 29, 55], [0, 51, 6], [0, 32, 57], [2, 45, 45]] ,
[[0, 50, 52], [0, 36, 30], [0, 50, 2], [0, 27, 47], [2, 45, 11]] ,
[[0, 51, 30], [0, 35, 53], [0, 52, 52], [0, 12, 47], [2, 33, 2]] ,
[[0, 51, 42], [0, 35, 2], [0, 51, 41], [0, 19, 35], [2, 38, 1]] ,
[[0, 53, 43], [0, 39, 8], [0, 52, 11], [0, 17, 59], [2, 43, 2]] ,
[[0, 53, 57], [0, 35, 43], [0, 52, 15], [0, 25, 26], [2, 47, 21]] ,
[[0, 50, 22], [0, 52, 52], [0, 51, 21], [0, 12, 56], [2, 47, 31]] ,
[[1, 31, 50], [1, 7, 42], [2, 39, 32]],
[[1, 29, 22], [1, 24, 46], [2, 54, 8]],
[[2, 35, 13], [0, 50, 17], [0, 34, 55], [0, 50, 24], [0, 19, 37]] ,
[[2, 45, 29], [0, 50, 8], [0, 39, 15], [0, 50, 16], [0, 25, 50]] ,
[[2, 42, 47], [0, 50, 2], [0, 39, 49], [0, 51, 53], [0, 21, 3]] ,
[[0, 50, 13], [0, 46, 2], [0, 51, 20], [0, 23, 47], [2, 51, 22]] ,
[[0, 52, 37], [0, 36, 15], [0, 51, 8], [0, 21, 44], [2, 41, 44]] ,
[[0, 50, 20], [0, 45, 32], [0, 50, 27], [0, 27, 53], [2, 54, 12]] ,
[[0, 53, 8], [0, 40, 54], [0, 50, 14], [0, 11, 23], [2, 35, 39]] ,
[[2, 50, 52], [0, 50, 24], [0, 51, 52], [0, 50, 0], [0, 18, 36]] ,
[[0, 50, 18], [0, 46, 0], [0, 50, 0], [0, 23, 33], [2, 49, 51]] ,
[[0, 52, 27], [0, 43, 41], [0, 50, 4], [0, 31, 11], [2, 57, 23]] ,
[[1, 2, 14], [0, 57, 15], [0, 46, 28]]   
]


path = 'C:\\Users\\Bomo\\Desktop\\VideoFolder'

for i in range(39):
    course_str = 'ch' + str(i+1)
    new_folder_path = path + '\\憲法' + str(i+1)
    os.mkdir(new_folder_path)
    print(new_folder_path)
    index = 0
    for idx,time_ in enumerate(LESSON_TIME[i]):
        lesson_str = 'l' + str(i+1) + '-' + str(idx+1)
        print(lesson_str)
   
        if not RECORDED[i][lesson_str]:
            print('未錄:' + lesson_str)
            goUrl(URL_COR, getUrl(course_str , lesson_str, i))
            record(time_, course_str, lesson_str, path, index)
            index = index + 1
    packVideo(course_str, path, new_folder_path)


# goUrl( [1505,51], getUrl('ch01', 'l1-1'))


