# 1. Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/
# 2. Пять раз кликните на кнопку Add Element
# 3. Соберите со страницы список кнопок Delete
# 4. Выведите на экран размер списка

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(2)


for i in range(5):
    add_elements = driver.find_element(By.CSS_SELECTOR, "button")
    add_elements.click()

delete_buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(f"Размер списка кнопок Delete: {len(delete_buttons)}")

sleep(3)
