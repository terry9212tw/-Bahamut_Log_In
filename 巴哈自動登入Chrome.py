from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
user_name = input()
pws = input()
path = Service('/Users/terryshih/Downloads/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options=options, service=path)

#登入
driver.get("https://user.gamer.com.tw/login.php")
time.sleep(5)
user = driver.find_element(by=By.NAME, value="userid")
password = driver.find_element(by=By.NAME, value="password")
user.send_keys(user_name)
password.send_keys(pws)
password.send_keys(Keys.RETURN)
# time.sleep(10)
time.sleep(5)
# Keys.F5
# WebDriverWait(driver, 60).until(
#     EC.presence_of_element_located((By.LINK_TEXT,  "signin-btn"))
# )

#簽到
# signin = driver.find_element(by=By.ID, value="signin-btn")
# # double_reward = driver.find_element(by=By., value="popup-dailybox__btn")
# signin.click()
# time.sleep(3)
# double_reward = driver.find_element_by_class_name("popup-dailybox__btn")
# double_reward.click()
# time.sleep(10)
# confirm = driver.find_element_by_class_name("btn btn-insert btn-primary")
# confirm.click()
