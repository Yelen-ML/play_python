import time
from selenium import webdriver 
for i in range(500):
    browser = webdriver.Edge() 
    browser.get("https://www.bilibili.com/video/...") #换成对应视频地址链接
    time.sleep(60) #播放时间，单位为秒
    browser.quit()