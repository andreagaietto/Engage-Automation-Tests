import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EngageLogin(unittest.TestCase):

    def setUp(self):
        #setting up by performing previous tests
        config = configparser.SafeConfigParser()
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
        print("setup")

    def test_no_username(self):
        #test that nothing happens when nothing entered for username
        driver = self.driver
        username = driver.find_element_by_id('id_username')
        username.clear()
        password = driver.find_element_by_id('id_password')
        password.clear()
        password.send_keys(self.password)
        username.send_keys(Keys.RETURN)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert self.databaseName.upper() in content.text
        print("test 1")

    def test_no_password(self):
        #test that nothing happens when nothing entered for password
        driver = self.driver
        username = driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_id('id_password')
        password.clear()
        username.send_keys(Keys.RETURN)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert self.databaseName.upper() in content.text

    def test_wrong_username(self):
        #test that northing happens when the wrong username is entered
        driver = self.driver
        username = driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys(self.username+"123")
        password = driver.find_element_by_id('id_password')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        content = driver.find_element_by_class_name('alert')
        assert "failed" in content.text

    def test_wrong_password(self):
        #test that northing happens when the wrong password is entered
        driver = self.driver
        username = driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_id('id_password')
        password.clear()
        password.send_keys(self.password+"123")
        password.send_keys(Keys.RETURN)
        content = driver.find_element_by_class_name('alert')
        assert "failed" in content.text

    def test_enter_username_password(self):
        #testing logging in
        driver = self.driver
        username = driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_id('id_password')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert "Dashboard" in content.text
        print("test 1")

    def tearDown(self):
        #closing down
        self.driver.close()
        print("close")

if __name__ == "__main__":
    unittest.main()