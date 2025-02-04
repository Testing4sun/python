# Откройте страницу http://the-internet.herokuapp.com/entry_ad
# В модальном окне нажмите на кнопку Сlose

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(1)

get_close = driver.find_element(By.CSS_SELECTOR, "div.modal-footer")
get_close.click()

driver.quit()
