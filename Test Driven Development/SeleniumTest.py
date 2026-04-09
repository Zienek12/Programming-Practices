from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestUsosLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.url = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYAf4362d1e09926264cfa0ca5e47b5a83ad9cd8142&locale=pl"
        self.input_name = "username"

    def tearDown(self):
        self.driver.close()

    def test_login_input_and_clear(self):
        driver = self.driver
        driver.get(self.url)
        
        try:
            login_box = driver.find_element(By.NAME, self.input_name)
        except Exception:
            self.fail("Couldnt find the login input box on the page.")

        test_value = "your_username"
        login_box.send_keys(test_value)
        
        input_value = login_box.get_attribute("value")
        self.assertEqual(test_value, input_value)

        
        try:
            clear_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Clear')]")
            clear_button.click()
            value_after_clear = login_box.get_attribute("value")
            self.assertEqual("", value_after_clear, "Box should be empty after clicking the clear button.")
        except Exception:
            self.fail("Couldnt find the clear button or it didnt work as expected.")
        sleep(2)
if __name__ == "__main__":
    unittest.main()