# Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# В поле ввода по локатору #delay введите значение 45
# Нажмите на кнопки:
    # 7
    # +
    # 8
    # =
# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(
           "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
           )

delay_input = driver.find_element(By.CSS_SELECTOR, '#delay')
delay_input.clear()
delay_input.send_keys('5')

buttons = driver.find_element(By.XPATH,
                              '//span[text()="7"]').click()
buttons = driver.find_element(By.XPATH,
                              '//span[text()="+"]').click()
buttons = driver.find_element(By.XPATH,
                              '//span[text()="8"]').click()
buttons = driver.find_element(By.XPATH,
                              '//span[text()="="]').click()

loading = WebDriverWait(driver, 60).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                     "div.screen"), '15'))


def test_calc():
    result = driver.find_element(By.CSS_SELECTOR,
                                 "div.screen").text
    assert result == '15'
