# WebAutomaiton
Web automation framework using python, selenium


2016/11/21
Made some changes on design pattern

Packaging page operations in parent class BasePage, like findelement:
    
    def findElement(self,element):
        '''
        Find element

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElement(element)
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type=="Id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type=="Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type=="Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type=="Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type=="Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type=="Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found"+ str(element))
        return elem

the sub class can inherit such functions and use them directly in its page operation:


    class GoogleMainPage(BasePage):
    """description of class"""
    searchbox = ('ID','lst-ib')

    def __init__(self, browser = 'chrome'):
        super().__init__(browser)
        
    def inputSearchContent(self,searchContent):
        searchBox = self.findElement(self.searchbox)
        self.type(searchBox,searchContent)
        self.enter(searchBox)
