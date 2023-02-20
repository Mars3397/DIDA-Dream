from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.parse

dict = {'a':float('1.5'),'b':float('3'),'c':float('2')}
print(dict)
print(list(dict)[0])
print(list(dict.values())[0])
print(list(dict)[1])
print(list(dict.values())[1])
print(list(dict)[2])
print(list(dict.values())[2])
sorted_footballers_by_goals = sorted(dict.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)
print(sorted_footballers_by_goals[0][1])
# print(list(dict)[0])
# print(list(dict.values())[0])
# print(list(dict)[1])
# print(list(dict.values())[1])
# print(list(dict)[2])
# print(list(dict.values())[2])

# query = 'https://spot.line.me/search/location?q=全家'
# url = urllib.parse.quote(query)
# print(url)

# options = Options()

# options.headless = True

# # driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
# # C:\james\chromedriver_win32
# driver = webdriver.Chrome("C:/james/chromedriver_win32/chromedriver.exe")

# driver.get("https://spot.line.me/search/location?q=%E5%85%A8%E5%AE%B6%E5%9F%BA%E9%9A%86%E7%B2%BE%E4%B8%80%E5%BA%97")

# button = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[3]/section/ul/li[1]/a/div/div/img")
# # time.sleep(5)
# print("button ",button)
# button.click()

# button = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[3]/section/ul/li[1]/a/div/div/img")
# time.sleep(5)
# button.click()

# print(driver.current_url)
# time.sleep(5)

# print("button ",button)
# driver.switch_to_window(driver.window_handles[-1])
# print(driver.current_url)

# print(driver.current_url)

# text = driver.find_element(By.XPATH, "/html/body/div/div/article/div[1]/div[1]/div[1]")
# text = driver.find_element_by_xpath("/html/body/div/div/article/div[1]/div[1]/div[1]")

