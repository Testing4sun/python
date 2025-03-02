from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.DataTypesForm import DataTypesForm
from pages.SlowCalculator import SlowCalculator
from pages.ClothesShop import ClothesShop


def test_data_types_form():
    driver = webdriver.Chrome()
    data_types_form = DataTypesForm(driver)
    data_types_form.go_to()

    data_types_form.first_name_form('Иван')
    data_types_form.last_name_form('Петров')
    data_types_form.address_form('Ленина, 55-3')
    data_types_form.email_form('test@skypro.com')
    data_types_form.phone_form('+7985899998787')
    data_types_form.zip_code_form('')
    data_types_form.city_form('Москва')
    data_types_form.country_form('Россия')
    data_types_form.job_position_form('QA')
    data_types_form.company_form('SkyPro')

    data_types_form.click_form()

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class"), (
        "Поле 'zip code' не подсвечено красным"
    )

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), (
            f"Поле {field_id} не подсвечено зеленым"
        )

    driver.quit()


def test_slow_calculator():
    driver = webdriver.Chrome()
    slow_calculator = SlowCalculator(driver)
    slow_calculator.go_to()

    slow_calculator.delay('5')

    slow_calculator.first_digit("7")
    slow_calculator.operation("+")
    slow_calculator.second_digit("8")
    slow_calculator.result_button()

    result = slow_calculator.get_result('15')
    assert result == '15'
    driver.quit()


def test_clothes_shop():
    driver = webdriver.Chrome()
    clothes_shop = ClothesShop(driver)
    clothes_shop.go_to()

    clothes_shop.user_name('standard_user')
    clothes_shop.password('secret_sauce')
    clothes_shop.login_button()

    clothes_shop.first_item('add-to-cart-sauce-labs-backpack')
    clothes_shop.second_item('add-to-cart-sauce-labs-bolt-t-shirt')
    clothes_shop.third_item('add-to-cart-sauce-labs-onesie')

    clothes_shop.go_to_cart()
    clothes_shop.checkout()
    clothes_shop.first_name_for_order('Ilya')
    clothes_shop.last_name_for_order('Ivanov')
    clothes_shop.first_name_for_order('Ilya')
    clothes_shop.postal_code_for_order('400000')
    clothes_shop.continue_for_order()

    total = clothes_shop.get_total()
    assert total == 'Total: $58.29'
    driver.quit()
