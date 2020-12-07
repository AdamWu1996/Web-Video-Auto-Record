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
        'ch1':'JqykbOKL',
        'ch2':'jlME4xle',
        'ch3':'VqoobVqZ',
        'ch4':'PKjRPkKw',
        'ch5':'Aq1gDpKn',
        'ch6':'GlA2xZqe',
        'ch7':'NlRMoLKw',
        'ch8':'zKVynpXD',
        'ch9':'MXNNR8XY',
        'ch10':'1lEz45qP',
        'ch11':'kXD5e8K8',
        'ch12':'Gl35N0Xd',
        'ch13':'xXr0PGla',
        'ch14':'dlY759Xy',
        'ch15':'8qkRP5ld',
        'ch16':'eqPj1NKB',
        'ch17':'pKGG83Kr',
        'ch18':'jKdAPrlp',
        'ch19':'VlJEDaKo',
        'ch20':'rlLVV3Xg',
        'ch21':'Yq200BKN',
        'ch22':'al6ZZmlr',
        'ch23':'bKbZZrK4',
        'ch24':'nXvAAOqY',
        'ch25':'WXW99plv',
        'ch26':'OKQAAEKZ',
        'ch27':'jKZggDlz',
        'ch28':'9lpddJl7',
        'ch29':'bl9nn1q4',
        'ch30':'NKammRKm',
        'ch31':'2KBaarXp',
        'ch32':'rl8OOgKV',
        'ch33':'mlmEE1lb',
        'ch34':'xX4vvPlO',
        'ch35':'YXeaa4XM',
        'ch36':'YK7gggKk',
        'ch37':'VXwmmglJ',
        'ch38':'zXxAA7K9',
        'ch39':'YX5go4l2'
    }

    LESSON_CODE = [
        
        {
         'l1-1':'NKao3Rqm',
         'l1-2':'bl99w1l4',
         'l1-3':'9lppNJl7'
         },
        
        {
         'l2-1':'mlmpL1Kb',
         'l2-2':'rl83xgKV',
         'l2-3':'2KB9prXp'
         },
        
        {
         'l3-1':'YK795gqk',
         'l3-2':'YXenp4KM',
         'l3-3':'xX49nPKO'
        },
        
        {
         'l4-1':'YX5rZ4K2',
         'l4-2':'zXxZy7l9',
         'l4-3':'VXwpMgKJ'
        },
        
        {'l5-1':'8lnpG8X7',
         'l5-2':'JXOyPDlV',
         'l5-3':'yKggrGKn'
         },
        
        {
         'l6-1':'jlMoYBXe',
         'l6-2':'JqypG3lL',
         'l6-3':'pq0e8ZXD'
        },
        
        {
         'l7-1':'Aq19BBqn',
         'l7-2':'PKjwGblw',
         'l7-3':'VqopGWXZ'
        },
        
			{
				'l8-1':'zKVwPolD',
				'l8-2':'NlROPkqw',
				'l8-3':'GlAYP3le'
			},

			{
				'l9-1':'kXD9P7K8',
				'l9-2':'MXNMP4qY',
				'l9-3':'1lEDPJKP'
			},
            
			{
				'l10-1':'8qk7Gmqd',
				'l10-2':'dlYDP5Ky',
				'l10-3':'xXrvGbXa',
				'l10-4':'Gl3d9zqd'
			},
            
			{
				'l11-1':'jKd0GBKp',
				'l11-2':'pKGNPEXr',
				'l11-3':'eqP0PVqB'
			},
            
			{
				'l12-1':'Yq29aBlN',
				'l12-2':'rlLjP3Xg',
				'l12-3':'GKzpGrqz',
				'l12-4':'VlJAPAKo'
			},
            
			{
				'l13-1':'nXv6GOXY',
				'l13-2':'al69QmKr',
				'l13-3':'bKbMPrX4'
			},
            
			{
				'l14-1':'jKZEPDXz',
				'l14-2':'OKQnPElZ',
				'l14-3':'WXW7kpXv'
			},
            
			{
				'l15-1':'bl99b1l4',
				'l15-2':'NKaoGRqm',
				'l15-3':'9lppGJl7'
			},
            
			{
				'l16-1':'mlmpG1Kb',
				'l16-2':'rl83vgKV',
				'l16-3':'2KB9PrXp'
			},
            
			{
				'l17-1':'YK79Wgqk',
				'l17-2':'YXenG4KM',
				'l17-3':'xX49pPKO'
			},
            
			{
				'l18-1':'yKgg1GKn',
				'l18-2':'YX5r84K2',
				'l18-3':'zXxZG7l9',
				'l18-4':'VXwpGgKJ'
			},
            
			{
				'l19-1':'pq0ewZXD', # 無自動播放
				'l19-2':'8lnpO8X7', # 無自動播放
				'l19-3':'JXOy5DlV'
			},
            
			{
				'l20-1':'NlRJrLlw', # 無自動播放
				'l20-2':'GlA8aZKe', # 無自動播放
				'l20-3':'Aq1eapqn'
			},
			{
				'l21-1':'1lEVx5qP',
				'l21-2':'MXNne8XY',
				'l21-3':'zKVJWpKD',
			},
			{
				'l22-1':'xXrJeGXa',
				'l22-2':'Gl37Z0ld',
				'l22-3':'kXDNW8l8',
			},
			{
				'l23-1':'pKGAx3qr',
				'l23-2':'eqPgMNlB',
				'l23-3':'8qkM45Kd',
                'l23-4':'dlYJG9qy'
			},
			{
				'l24-1':'jKdNprqp',
				'l24-2':'rlLy9eqg',
				'l24-3':'GKz24EKz',
                'l24-4':'VlJo9aqo'
			},
			{
				'l25-1':'nXv8wRlY',
				'l25-2':'bKbDJmq4',
				'l25-3':'al6mvYKr',
                'l25-4':'Yq2wjEXN'
			},
			{
				'l26-1':'jKZdW6qz',
				'l26-2':'OKQ5MnKZ',
				'l26-3':'WXWJgYqv'
			},
			{
				'l27-1':'2KBDW8qp',
				'l27-2':'NKaJZJlm',
				'l27-3':'bl9ZBaq4',
                'l27-4':'9lpg3QK7'
			},
			{
				'l28-1':'YXeVxwKM',
				'l28-2':'xX4wPOqO',
				'l28-3':'mlm0d4Kb',
                'l28-4':'rl8wB4KV'
			},
			{
				'l29-1':'YX5wBnl2',
				'l29-2':'zXx8wVX9',
				'l29-3':'VXw2wxqJ',
                'l29-4':'YK7pBxlk'
			},
			{
				'l30-1':'pq07GjlD',
				'l30-2':'8lnnZZl7',
				'l30-3':'JXOO61XV',
                'l30-4':'yKgAEWqn',
			},
			{
				'l31-1':'VqoO7VqZ',
				'l31-2':'jlM03xKe',
				'l31-3':'Jqy96OqL',
			},
			{
				'l32-1':'Aq1egpqn',
				'l32-2':'GlA82ZKe',
				'l32-3':'PKjoRklw',
			},
			{
				'l33-1':'MXNnN8XY',
				'l33-2':'NlRJMLlw',
				'l33-3':'zKVJypKD',
			},
			{
				'l34-1':'1lEVz5qP',
				'l34-2':'xXrJ0GXa',
				'l34-3':'Gl3750ld',
                'l34-4':'kXDN58l8'
			},
			{
				'l35-1':'pKGAG3qr',
				'l35-2':'eqPgjNlB',
				'l35-3':'8qkMR5Kd',
                'l35-4':'dlYJ79qy'
			},
			{
				'l36-1':'rlLyDeqg',
				'l36-2':'GKz2jEKz',
				'l36-3':'VlJoEaqo',
                'l36-4':'jKdNArqp'
			},
			{
				'l37-1':'Yq2w3EXN'
			},
			{
				'l38-1':'bKbDpmq4'
			},
			{
				'l39-1':'WXWJ5Yqv',
                'l39-2':'OKQ5GnKZ'
			}
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
    return T.sleep(3600*h + 60*m + s)

def record(time, course, lesson, path):
    print('starting...')
    pyautogui.press('f2')
    waitTime(0, 0, 5)
    autoPlay()
    waitTime(time[0], time[1], time[2])
    print('ending')
    waitTime(0, 0, 5)
    pyautogui.press('f2')
    waitTime(0, 0, 3)
    _, _, files = os.walk(path).__next__()
    _, extension = os.path.splitext(files[0])
    file_path = path + '\\' + files[0]
    dest_path = path + '\\' + course + '-' + lesson + extension
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

def packVideo(course, path):
    _, _, files = os.walk(path).__next__()
    folder_path = path + '\\' + course
    os.mkdir(folder_path)
    for file in files:
        shutil.move(path + '\\' + file, folder_path)



# URL_COR = [1505, 51]
URL_COR = [1302, 61]
RECORDED = [
       {
				'l1-1':True,
				'l1-2':True,
				'l1-3':True
			},
			{
				'l2-1':True,
				'l2-2':True,
				'l2-3':True
			},
			{
				'l3-1':True,
				'l3-2':True,
				'l3-3':True
			},
			{
				'l4-1':True,
				'l4-2':True,
				'l4-3':True
			},
			{
				'l5-1':True,
				'l5-2':True,
				'l5-3':True
			},
			{
				'l6-1':True,
				'l6-2':True,
				'l6-3':True
			},
			{
				'l7-1':True,
				'l7-2':True,
				'l7-3':True
			},
			{
				'l8-1':False,
				'l8-2':False,
				'l8-3':False
			},
			{
				'l9-1':False,
				'l9-2':False,
				'l9-3':False
			},
			{
				'l10-1':True,
				'l10-2':True,
				'l10-3':True,
                'l10-4':False
			},
			{
				'l11-1':True,
				'l11-2':True,
				'l11-3':True
			},
			{
				'l12-1':True,
				'l12-2':True,
				'l12-3':True,
            'l12-4':True
			},
			{
				'l13-1':True,
				'l13-2':True,
				'l13-3':True
			},
			{
				'l14-1':True,
				'l14-2':True,
				'l14-3':True
			},
			{
				'l15-1':True,
				'l15-2':True,
				'l15-3':True
			},
			{
				'l16-1':True,
				'l16-2':True,
				'l16-3':True
			},
			{
				'l17-1':True,
				'l17-2':True,
				'l17-3':True
			},
			{
				'l18-1':True,
				'l18-2':True,
				'l18-3':True,
            'l18-4':True
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
				'l21-3':True
			},
			{
				'l22-1':True,
				'l22-2':True,
				'l22-3':True
			},
			{
				'l23-1':True,
				'l23-2':True,
				'l23-3':True,
            'l23-4':True
			},
			{
				'l24-1':True,
				'l24-2':True,
				'l24-3':True,
            'l24-4':True
			},
			{
				'l25-1':True,
				'l25-2':True,
				'l25-3':True,
            'l25-4':True
			},
			{
				'l26-1':True,
				'l26-2':True,
				'l26-3':True
			},
			{
				'l27-1':True,
				'l27-2':True,
				'l27-3':True,
				'l27-4':True,
			},
			{
				'l28-1':True,
				'l28-2':True,
				'l28-3':True,
				'l28-4':True,
			},
			{
				'l29-1':True,
				'l29-2':True,
				'l29-3':True,
				'l29-4':True,
			},
			{
				'l30-1':True,
				'l30-2':True,
				'l30-3':True,
				'l30-4':True,
			},
			{
				'l31-1':True,
				'l31-2':True,
				'l31-3':True
			},
			{
				'l32-1':True,
				'l32-2':True,
				'l32-3':True
			},
			{
				'l33-1':False,
				'l33-2':False,
				'l33-3':False
			},
			{
				'l34-1':True,
				'l34-2':True,
				'l34-3':True,
            'l34-4':True
			},
			{
				'l35-1':True,
				'l35-2':True,
				'l35-3':True,
            'l35-4':True
			},
			{
				'l36-1':True,
				'l36-2':False,
				'l36-3':False,
            'l36-4':False
			},
			{
				'l37-1':False
			},
			{
				'l38-1':False
			},
			{
				'l39-1':False,
				'l39-2':False
			}
    ]

LESSON_TIME = [ [ [0,59,1], [1,1,55], [0,45,57] ], # 01
        [ [0,59,34], [0,59,10], [0,57,10] ], # 01
        [ [0,58,50], [1,3,41], [0,55,42] ], # 01
        [ [0,49,46], [0,56,59], [1,7,34] ], # 01
        [ [0,52,29], [0,53,1], [0,59,18] ], # 01
        [ [0,56,1], [0,56,46], [1,0,20] ], # 01
        [ [0,55,1], [0,53,8], [0,53,18] ], # 01
        [ [0,58,43], [0,54,58], [0,55,19] ], # 01
        [ [0,58,35], [0,56,25], [0,53,20] ], # 01
        [ [0,50,2], [0,55,36], [0,50,5], [0,15,45]  ], # 01
        [ [0,56,44], [0,58,52], [1,2,26] ], # 01
        [ [0,48,58], [0,53,30], [0,51,3], [0,15,55]  ], # 01
        [ [0,51,19], [0,55,5], [1,4,55] ], # 01
        [ [0,55,30], [0,54,18], [1,5,13] ], # 01
        [ [0,58,6], [0,56,33], [0,59,33] ], # 01
        [ [0,58,48], [0,50,15], [0,59,26] ], # 01
        [ [0,56,31], [0,55,28], [0,55,14] ], # 01
        [ [0,55,56], [0,55,17], [0,50,20], [0,13,19]  ], # 01
        [ [0,58,20], [0,58,27], [1,2,4] ], # 01
        [ [0,59,11], [0,54,1], [0,59,40] ], # 01
        [ [0,57,24], [0,58,59], [0,54,35] ], # 01
        [ [0,51,36], [0,59,6], [0,58,32] ], # 01
        [ [0,46,40], [0,47,1], [0,39,8], [0,39,18]  ], # 01
        [ [0,54,33], [0,53,33], [0,51,31], [0,11,40]  ], # 01
        [ [0,59,51], [0,53,19], [0,48,19], [0,12,10]  ], # 01
        [ [0,51,50], [0,59,22], [0,59,45] ], # 01
        [ [0,46,26], [0,52,40], [0,30,10], [0,42,44]  ], # 01
        [ [0,47,2], [0,47,4], [0,39,37], [0,39,50]  ], # 01
        [ [0,49,44], [0,51,41], [0,49,15], [0,20,55]  ], # 01
        [ [0,51,33], [0,50,12], [0,31,11], [0,31,34]  ], # 01
        [ [0,49,52], [1,2,15], [1,1,49] ], # 01
        [ [0,58,11], [0,56,22], [0,58,42] ], # 01
        [ [0,50,2], [0,49,37], [1,11,15] ], # 01
        [ [0,50,0], [0,40,6], [0,50,47], [0,30,18]  ], # 01
        [ [0,48,50], [0,50,59], [0,33,6] ], # 01
        [ [0,32,25] ], # 01
        [ [0,51,40] ], # 01
        [ [0,58,13] ], # 01
        [ [0,50,10], [0,25,5] ]
    ]


path = 'C:\\Users\\wubomo\\Desktop\\VideoFolder'

for i in range(20):
    course_str = 'ch' + str(i+1)
    new_folder_path = path + '\\法學大意' + str(i+1)
    os.mkdir(new_folder_path)
    print(new_folder_path)
    
    for idx,time_ in enumerate(LESSON_TIME2[i]):
        lesson_str = 'l' + str(i+1) + '-' + str(idx+1)
        print(lesson_str)
   
        if not RECORDED[i][lesson_str]:
            print('未錄:' + lesson_str)
            goUrl(URL_COR, getUrl(course_str , lesson_str, i))
            record(time_, course_str, lesson_str, path)
            
    packVideo(course_str, path)


# goUrl( [1505,51], getUrl('ch01', 'l1-1'))



