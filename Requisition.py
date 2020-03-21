import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class creating_requisition(unittest.TestCase): 

    def setUp(self):
        #setting up by performing previous tests to get to correct point
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.databaseName = config.get('DEFAULT', 'databaseName')
        self.url = config.get('DEFAULT', 'url')
        self.username = config.get('DEFAULT', 'username')
        self.password = config.get('DEFAULT', 'password')
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        database = self.driver.find_element_by_id('id_database')
        database.clear()
        database.send_keys(self.databaseName)
        database.send_keys(Keys.RETURN)
        username = self.driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys(self.username)
        password = self.driver.find_element_by_id('id_password')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        specimen = self.driver.find_element_by_link_text('Specimens')
        specimen.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector("form input[name^='vial.bsi_id:']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("fa-check").click()
        self.driver.find_element_by_class_name("fa-shopping-cart").click()

    def test_creating_requisition(self):
        #selecting create requisition button
        driver = self.driver
        driver.find_element_by_class_name("fa-plus").click()
        content = driver.find_element_by_css_selector('.page-header h2')
        assert "New Requisition" in content.text

    def tearDown(self):
        #closing down
        self.driver.close()
        print("close")

if __name__ == "__main__":
    unittest.main()