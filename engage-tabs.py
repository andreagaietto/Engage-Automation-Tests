import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EngageTabs(unittest.TestCase):
    
    def setUp(self):
        #setting up by performing previous tests
        self.databaseName = "" #TODO: replace with settings
        self.username = "" #TODO: replace with settings
        self.password = "" #TODO: replace with settings
        self.driver = webdriver.Chrome()
        self.driver.get("https://engage-uat.bsisystems.com/")
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
        print("setup")

    def test_select_specimen_tab(self):
        #test the you can select specimens tab
        driver = self.driver
        specimen = driver.find_element_by_link_text('Specimens')
        specimen.send_keys(Keys.RETURN)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert "Specimen Search" in content.text
        print("test 1")

    def test_select_requisitions_tab(self):
        #test that you can select requisitions tab
        driver = self.driver
        requisitions = driver.find_element_by_link_text('Requisitions')
        requisitions.send_keys(Keys.RETURN)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert "Requisition Search" in content.text
        
    def test_select_shipments_tab(self):
        #test that you can select shipments tab
        driver = self.driver
        shipments = driver.find_element_by_link_text('Shipments')
        shipments.send_keys(Keys.RETURN)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert "Shipment Search" in content.text

    def test_cart_tab(self):
        #test that you can select cart tab
        driver = self.driver
        driver.find_element_by_class_name("fa-shopping-cart").click()
        #driver.implicitly_wait(2)
        content = driver.find_element_by_css_selector('.page-header h2')
        assert "Specimen Cart" in content.text

    def test_settings_menu(self):
        #test that you can select settings from the dropdown menu
        driver = self.driver
        driver.implicitly_wait(2)
        driver.find_element_by_link_text("Kryo Test").click()
        driver.find_element_by_xpath('//a[@href="/'+self.databaseName+'/profile/"]').click()
        content = driver.find_element_by_css_selector('.page-header h2')
        assert "Profile" in content.text


    def tearDown(self):
        #closing down
        self.driver.close()
        print("close")

if __name__ == "__main__":
    unittest.main()