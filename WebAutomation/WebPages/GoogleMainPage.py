from BasePage import BasePage



class GoogleMainPage(BasePage):
    """description of class"""
    searchbox = ('ID','lst-ib')

    
    def __init__(self, browser = 'chrome'):
        super().__init__(browser)
        

    
    def inputSearchContent(self,searchContent):
        searchBox = self.findElements(self.searchbox)
        self.type(searchBox[0],searchContent)
        self.enter(searchBox[0])
        #searchBox = self.driver.find_element(*self.searchbox)
        #searchBox.send_keys(searchContent+Keys.RETURN)




