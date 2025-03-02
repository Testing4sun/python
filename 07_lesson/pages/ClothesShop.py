from selenium.webdriver.common.by import By


class ClothesShop:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get("https://www.saucedemo.com/")

    def user_name(self, term):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#user-name').send_keys(term)

    def password(self, term):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#password').send_keys(term)

    def login_button(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#login-button').click()

    def first_item(self, term):
        self.driver.find_element(By.ID, term).click()

    def second_item(self, term):
        self.driver.find_element(By.ID, term).click()

    def third_item(self, term):
        self.driver.find_element(By.ID, term).click()

    def go_to_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()

    def first_name_for_order(self, term):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#first-name').send_keys(term)

    def last_name_for_order(self, term):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#last-name').send_keys(term)

    def postal_code_for_order(self, term):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#postal-code').send_keys(term)

    def continue_for_order(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input#continue').click()

    def get_total(self):
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         "div.summary_info div.summary_total_label"
                                         ).text
        return total
