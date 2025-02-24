# Перейдите на сайт
    #https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
# Дождитесь загрузки всех картинок
# Получите значение атрибута src у 3-й картинки
# Выведите значение в консоль

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


loading = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#award")
        )
    )

src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
print(src)

driver.quit()
