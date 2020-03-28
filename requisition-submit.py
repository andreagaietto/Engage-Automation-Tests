import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class requisition_submit(unittest.TestCase):

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
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("form input[name^='vial.bsi_id:']").click()
        self.driver.find_element_by_class_name("fa-check").click()
        self.driver.find_element_by_class_name("fa-shopping-cart").click()
        self.driver.get(self.driver.find_element_by_css_selector(".page-header .action-btns .btn:nth-child(2)").get_attribute("href"))
        self.driver.implicitly_wait(5)

  def test_add_info_to_requisition(self):
        #adding all required information into the requisition fields to test submit functionality
        driver = self.driver
        driver.find_element_by_css_selector("#s2id_id_req_repository\.repos_id .select2-choice").click()
        subContainerClass = "#select2-drop:not([style*='display: none'])"
        repository = driver.find_element_by_css_selector(subContainerClass + " .select2-input")    
        repository.send_keys("Kryosphere")
        selectItem = driver.find_element_by_css_selector(subContainerClass + " .select2-results li.select2-result-selectable")
        selectItem.click()
        driver.find_element_by_css_selector(".form-actions .btn:nth-child(1)").click()
        driver.implicitly_wait(5)


      

  def tearDown(self):
        #closing down
        self.driver.quit()
        print("close")

if __name__ == "__main__":
    unittest.main()
