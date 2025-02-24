# Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# Заполните форму значениями
    # First name Иван
    # Last name Петров
    # Address Ленина, 55-3
    # Email test@skypro.com
    # Phone number +7985899998787
    # Zip code *оставить пустым
    # City Москва
    # Country Россия
    # Job position QA
    # Company SkyPro
# Нажмите кнопку Submit
# Проверьте (assert), что поле Zip code подсвечено красным
# Проверьте (assert), что остальные поля подсвечены зеленым

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get(
           "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
           )


first_name_input = driver.find_element(By.CSS_SELECTOR,
                                       'input[name="first-name"]'
                                       ).send_keys('Иван')
last_name_input = driver.find_element(By.CSS_SELECTOR,
                                      'input[name="last-name"]'
                                      ).send_keys('Петров')
address_input = driver.find_element(By.CSS_SELECTOR,
                                    'input[name="address"]'
                                    ).send_keys('Ленина, 55-3')
email_input = driver.find_element(By.CSS_SELECTOR,
                                  'input[name="e-mail"]'
                                  ).send_keys('test@skypro.com')
phone_input = driver.find_element(By.CSS_SELECTOR,
                                  'input[name="phone"]'
                                  ).send_keys('+7985899998787')
zip_code_input = driver.find_element(By.CSS_SELECTOR,
                                     'input[name="zip-code"]'
                                     ).send_keys('')
city_input = driver.find_element(By.CSS_SELECTOR,
                                 'input[name="city"]'
                                 ).send_keys('Москва')
country_input = driver.find_element(By.CSS_SELECTOR,
                                    'input[name="country"]'
                                    ).send_keys('Россия')
job_position_input = driver.find_element(By.CSS_SELECTOR,
                                         'input[name="job-position"]'
                                         ).send_keys('QA')
company_input = driver.find_element(By.CSS_SELECTOR,
                                    'input[name="company"]'
                                    ).send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR,
                             'button.btn.btn-outline-primary.mt-3').click()


def test_form():
    assert "alert-danger" in driver.find_element(By.ID, "zip-code"
                                                 ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "first-name"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "last-name"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "address"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "e-mail"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "phone"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "city"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "country"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "job-position"
                                                  ).get_attribute("class")
    assert "alert-success" in driver.find_element(By.ID,
                                                  "company"
                                                  ).get_attribute("class")
