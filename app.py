from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import win32gui
import win32con
import win32api
import pyautogui

##chrome_options = Options()
##chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
 
##mobile_emulation = { "deviceName": "Galaxy S5" }
 
##chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
##driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
chrome_options = Options()
chrome_options.add_argument('--incognito')  ## 시크릿 모드 
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.instagram.com/')


time.sleep(4)

e = driver.find_element_by_name('username')   ##아이디
e.send_keys('')  ##키입력 


e = driver.find_element_by_name('password')   ##패스워드
e.send_keys('')


time.sleep(2)
e.send_keys(Keys.ENTER)  ##엔터


time.sleep(10)
e = driver.find_elements_by_class_name('_8-yf5')[2]   ##게시물등록

e.click()  ##클릭 

time.sleep(3)
e = driver.find_elements_by_class_name('sqdOP')[2]    ##파일 선택
e.click()  ##클릭 


time.sleep(2)
w = win32gui.GetWindowText(win32gui.GetForegroundWindow())   ##파일창 제어

time.sleep(2)
hwnd = win32gui.FindWindow(None,'열기')
time.sleep(2)
edit = win32gui.GetDlgItem(hwnd, 0x47C)
buttonid = win32gui.GetDlgItem(hwnd, 0x1)



pyautogui.write('D:\gameDev\AndroidGame\DDongAgi_1\Assets\Atest11.png', interval=0.1) # 각 문자를 0.25마다 타이핑합니다.   ##파일명 입력(경로포함)

time.sleep(3)
win32api.PostMessage(buttonid, win32con.WM_LBUTTONDOWN, 0, 0)  ##(열 기 클리)
win32api.Sleep(100)
win32api.PostMessage(buttonid, win32con.WM_LBUTTONUP, 0, 0) ##(열기 클리)
win32api.Sleep(100)

time.sleep(2)
e = driver.find_elements_by_class_name('sqdOP')[2]  ##파일등록중 다음
e.click()  ##클릭 
time.sleep(2)
e = driver.find_elements_by_class_name('sqdOP')[2]  ##파일등록중 2번째 다음
e.click()  ##클릭 

time.sleep(2)
e = driver.find_elements_by_class_name('lFzco')[0]  ##본문내용 작성란
e.send_keys('안녕하세요 게시물 올리기 연습 중입니다. 좋은 하루 보내세요')  


time.sleep(2)
e = driver.find_elements_by_class_name('sqdOP')[2]  ##최종 게시하기 버튼
e.click()  ##클릭 