import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Specimen_Select_Screen(unittest.TestCase): 

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
 
    def test_selecting_first_item(self):
        #selecting first item under specimen search
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_css_selector("form input[name^='vial.bsi_id:']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_class_name("fa-check").click()
        driver.find_element_by_class_name("fa-shopping-cart").click()
        cart = driver.find_element_by_css_selector('.search-title h3')
        assert "Individual Specimens" in cart.text

    def test_clearing_cart(self):
        #testing clearing items from cart
        driver = self.driver
        driver.find_element_by_class_name("fa-shopping-cart").click()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("fa-trash").click()
        cart = driver.find_element_by_class_name("alert-success")
        assert "emptied" in cart.text

    def test_clearing_cart_from_specimen_screen(self):
        #testing clearing cart from specimens screen
        driver = self.driver
        driver.implicitly_wait(3)
        driver.find_element_by_css_selector("form input[name^='vial.bsi_id:']").click()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("hidden-xs").click()
        cart = driver.find_element_by_class_name("cart-total")
        assert "0" in cart.text





def tearDown(self):
        #closing down
        self.driver.quit()
        print("close")

if __name__ == "__main__":
    unittest.main()