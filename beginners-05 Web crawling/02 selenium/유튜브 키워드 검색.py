from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.youtube.com/")
driver.implicitly_wait(500)

time.sleep(3)

# 검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//*[@id="search"]')

# search 변수에 저장된 곳에 값을 전송
search.send_keys("노마드 코더")
time.sleep(1)

# search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)
