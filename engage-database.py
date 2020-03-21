import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EngageDatabase(unittest.TestCase):

    def setUp(self):
        #navigating to correct website and starting up webdriver
        config = configparser.SafeConfigParser()
        config.read('config.ini')
        self.databaseName = config.get('DEFAULT', 'databaseName')
        self.url = config.get('DEFAULT', 'url')
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        print("setup")

    def test_access_engage(self):
        #checking to make sure website is correct via content on page
        driver = self.driver
        self.assertIn("Engage", driver.title)
        content = driver.find_element_by_css_selector('.page-header h1')
        assert "BSI Engage" in content.text
        print("test 1")

    def test_wrong_database(self):
        #testing input of wrong database name
        driver = self.driver
        database = driver.find_element_by_id('id_database')
        database.clear()
        database.send_keys(self.databaseName+"123")
        database.send_keys(Keys.RETURN)
        driver.implicitly_wait(2)
        content = driver.find_element_by_class_name('alert')
        assert "error" in content.text
        print("test 2")

    def test_no_database(self):
        #testing null database name
        driver = self.driver
        database = driver.find_element_by_id('id_database')
        database.clear()
        database.send_keys(Keys.RETURN)
        driver.implicitly_wait(2)
        content = driver.find_element_by_class_name('alert')
        assert "name" in content.text
        print("test 3")
    

    def test_database_name(self):
        #entering database information and verifying acceptance
        driver = self.driver
        database = driver.find_element_by_id('id_database')
        database.clear()
        database.send_keys(self.databaseName)
        database.send_keys(Keys.RETURN)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert self.databaseName.upper() in content.text

        print("test 4")

    def tearDown(self):
        #closing webdriver
        self.driver.close()
        print("close")

if __name__ == "__main__":
    unittest.main()