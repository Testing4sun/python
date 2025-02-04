# Откройте страницу http://uitestingplayground.com/classattr.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
# P. s. Имеется в виду ручной запуск скрипта, цикл в коде не нужен.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
sleep(1)

blue_buttton = driver.find_element(By.CSS_SELECTOR,
                                   "button.btn.class1.btn-primary.btn-test")
blue_buttton.click()

driver.quit()


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
sleep(1)

blue_buttton = driver.find_element(By.CSS_SELECTOR,
                                   "button.btn.class1.btn-primary.btn-test")
blue_buttton.click()

driver.quit()


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
sleep(1)

blue_buttton = driver.find_element(By.CSS_SELECTOR,
                                   "button.btn.class1.btn-primary.btn-test")
blue_buttton.click()

driver.quit()
