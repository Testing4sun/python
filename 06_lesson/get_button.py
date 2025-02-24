# Перейдите на страницу http://uitestingplayground.com/ajax
# Нажмите на синюю кнопку
# Получите текст из зеленой плашки
# Выведите его в консоль ("Data loaded with AJAX get request.")

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

green_line_text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(green_line_text)

driver.quit()
