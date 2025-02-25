from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


def test_shop():
    driver.find_element(By.CSS_SELECTOR,
                        'input#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR,
                        'input#password').send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR,
                        'input#login-button').click()

    driver.find_element(By.CSS_SELECTOR,
                        'button#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR,
                        'button#add-to-cart-sauce-labs-bolt-t-shirt'
                        ).click()
    driver.find_element(By.CSS_SELECTOR,
                        'button#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR,
                        'div#shopping_cart_container a.shopping_cart_link'
                        ).click()

    driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()

    driver.find_element(By.CSS_SELECTOR,
                        'input#first-name').send_keys('Ilya')
    driver.find_element(By.CSS_SELECTOR,
                        'input#last-name').send_keys('Ivanov')
    driver.find_element(By.CSS_SELECTOR,
                        'input#postal-code').send_keys('400000')

    driver.find_element(By.CSS_SELECTOR, 'input#continue').click()
    total = driver.find_element(By.CSS_SELECTOR,
                                "div.summary_info div.summary_total_label"
                                ).text
    driver.quit()
    assert total == 'Total: $58.29'
