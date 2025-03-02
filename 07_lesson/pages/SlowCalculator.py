from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculator:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(
           "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
           )

    def delay(self, term):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(term)

    def first_digit(self, term):
        self.driver.find_element(By.XPATH, f"//span[text()='{term}']").click()

    def operation(self, term):
        self.driver.find_element(By.XPATH, f"//span[text()='{term}']").click()

    def second_digit(self, term):
        self.driver.find_element(By.XPATH, f"//span[text()='{term}']").click()

    def result_button(self):
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def get_result(self, term):
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(
                                    (By.CSS_SELECTOR, "div.screen"), term)
                                    )
        result = self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result
