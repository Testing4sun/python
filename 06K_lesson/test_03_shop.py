# Откройте сайт магазина: https://www.saucedemo.com/
# Авторизуйтесь как пользователь standard_user
# Добавьте в корзину товары:
    # Sauce Labs Backpack
    # Sauce Labs Bolt T-Shirt
    # Sauce Labs Onesie
# Перейдите в корзину
# Нажмите Checkout
# Заполните форму своими данными:
    # имя
    # фамилия
    # почтовый индекс
# Нажмите кнопку Continue.
# Прочитайте со страницы итоговую стоимость ( Total )
# Закройте браузер
# Проверьте, что итоговая сумма равна $58.29

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_input = driver.find_element(By.CSS_SELECTOR,
                                     'input#user-name'
                                     ).send_keys('standard_user')
password_input = driver.find_element(By.CSS_SELECTOR,
                                     'input#password'
                                     ).send_keys('secret_sauce')

button = driver.find_element(By.CSS_SELECTOR,
                             'input#login-button').click()

button = driver.find_element(By.CSS_SELECTOR,
                             'button#add-to-cart-sauce-labs-backpack').click()
button = driver.find_element(By.CSS_SELECTOR,
                             'button#add-to-cart-sauce-labs-bolt-t-shirt'
                             ).click()
button = driver.find_element(By.CSS_SELECTOR,
                             'button#add-to-cart-sauce-labs-onesie').click()

button = driver.find_element(By.CSS_SELECTOR,
                             'div#shopping_cart_container a.shopping_cart_link'
                             ).click()

button = driver.find_element(By.CSS_SELECTOR,
                             'button#checkout').click()

first_name_input = driver.find_element(By.CSS_SELECTOR,
                                       'input#first-name').send_keys('Ilya')
last_name_input = driver.find_element(By.CSS_SELECTOR,
                                      'input#last-name').send_keys('Ivanov')
postal_code_input = driver.find_element(By.CSS_SELECTOR,
                                        'input#postal-code'
                                        ).send_keys('400000')

button = driver.find_element(By.CSS_SELECTOR, 'input#continue').click()


def test_shop():
    total = driver.find_element(By.CSS_SELECTOR,
                                "div.summary_info div.summary_total_label"
                                ).text
    driver.quit()
    assert total == 'Total: $58.29'
