# Откройте страницу http://uitestingplayground.com/dynamicid.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
# P. s. Имеется в виду ручной запуск скрипта, цикл в коде не нужен.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(1)

dynamic_id = driver.find_element(By.CSS_SELECTOR,
                                 "button[name='Button with Dynamic ID']")
dynamic_id.click()

driver.quit()


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(1)

dynamic_id = driver.find_element(By.CSS_SELECTOR,
                                 "button[name='Button with Dynamic ID']")
dynamic_id.click()

driver.quit()


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(1)

dynamic_id = driver.find_element(By.CSS_SELECTOR,
                                 "button[name='Button with Dynamic ID']")
dynamic_id.click()

driver.quit()
