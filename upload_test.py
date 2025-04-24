import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CRED = dict(admin='admin')

class TestGeolocation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_click_geolocation_button(self):
        user = "admin"
        password = CRED["admin"]
        url = f"https://{user}:{password}@the-internet.herokuapp.com/geolocation"
        driver = self.driver
        driver.get(url)
        time.sleep(2)  
        button = driver.find_element(By.XPATH, "//button[text()='Where am I?']")
        button.click()       
        time.sleep(5)
        result = driver.find_element(By.ID, "demo")
        print("Geolocation Result:", result.text)

        self.assertIn("Longitude", result.text)  
        self.assertNotEqual(result.text.strip(), "")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
