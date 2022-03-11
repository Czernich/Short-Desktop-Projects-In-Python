from selenium import webdriver
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSckwcX9cnxi7cEqAWvPfqrfePHDsl6zkM1dZMQHDHoj_xWy1g/viewform?usp=sf_link"
driver_path = "D:\pythonProject\ChromeDrivers\chromedriver.exe"


class SaveData:
    def __init__(self, link, address, price):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get(FORM_URL)
        time.sleep(3)

        self.link = link
        self.address = address
        self.price = price

    def import_data(self):
        address = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        address.send_keys(self.address)

        price = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        price.send_keys(self.price)

        link = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        link.send_keys(self.link)
        time.sleep(1)
        send_btn = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
        )
        send_btn.click()
        time.sleep(1)
        self.driver.quit()

