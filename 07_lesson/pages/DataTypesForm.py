from selenium.webdriver.common.by import By


class DataTypesForm:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    def first_name_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]'
                                 ).send_keys(term)

    def last_name_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]'
                                 ).send_keys(term)

    def address_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="address"]'
                                 ).send_keys(term)

    def email_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]'
                                 ).send_keys(term)

    def phone_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]'
                                 ).send_keys(term)

    def zip_code_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]'
                                 ).send_keys(term)

    def city_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="city"]'
                                 ).send_keys(term)

    def country_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="country"]'
                                 ).send_keys(term)

    def job_position_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]'
                                 ).send_keys(term)

    def company_form(self, term):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="company"]'
                                 ).send_keys(term)

    def click_form(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button.btn.btn-outline-primary.mt-3').click()
