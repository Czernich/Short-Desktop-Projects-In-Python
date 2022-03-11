from selenium import webdriver
import time

driver_path = "D:\pythonProject\ChromeDrivers\chromedriver.exe"
URL = 'https://docs.google.com/forms/d/1XINxqRdIvxiqn7jjdQC_YEAaPeyJT5oZ26Ab63MijFc/edit#responses'


class ShowExcel:
    def __init__(self):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get(URL)
        time.sleep(3)

        to_excel = self.driver.find_element_by_class_name("freebirdMaterialIconIconEl")
        to_excel.click()
