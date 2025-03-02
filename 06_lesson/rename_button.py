# Перейдите на сайт http://uitestingplayground.com/textinput
# Укажите в поле ввода текст SkyPro
# Нажмите на синюю кнопку
# Получите текст кнопки и выведите в консоль ("SkyPro")

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

my_text = "SkyPro"
skypro_input = driver.find_element(By.CSS_SELECTOR,
                                   'input.form-control').send_keys(my_text)

button = driver.find_element(By.CSS_SELECTOR,
                             'div.form-group button#updatingButton').click()

new_text = driver.find_element(By.CSS_SELECTOR,
                               "div.form-group button#updatingButton").text

print(new_text)

driver.quit()
