# Откройте страницу http://the-internet.herokuapp.com/login
# В поле username введите значение tomsmith
# В поле password введите значение SuperSecretPassword!
# Нажмите кнопку Login

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

username_input = "input#username"
username_input = driver.find_element(By.CSS_SELECTOR, username_input)
username_input.send_keys("tomsmith")
sleep(1)

password_input = "input#password"
password_input = driver.find_element(By.CSS_SELECTOR, password_input)
password_input.send_keys("SuperSecretPassword!")
sleep(1)

get_login = driver.find_element(By.CSS_SELECTOR, ".radius")
get_login.click()
sleep(2)

driver.quit()
