from BasePage import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleMainPage(BasePage):
    """description of class"""
    searchbox = (By.ID,'lst-ib')

    def inputSearchContent(self,searchContent):
        searchBox = self.driver.find_element(*self.searchbox)
        searchBox.send_keys(searchContent+Keys.RETURN)




