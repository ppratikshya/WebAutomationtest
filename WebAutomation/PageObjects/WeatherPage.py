import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WeatherPage:

    def __init__(self, driver):
        self.driver = driver


    Searchcity = (By.XPATH, "//input[@data-testid='searchModalInputBox']")

    TemperatureSearch=(By.XPATH,"//span[@data-testid='TemperatureValue']")

    def ActionSearchcity(self,text):
        self.driver.find_element(*WeatherPage.Searchcity).send_keys(text)
        time.sleep(2)
        self.driver.find_element(*WeatherPage.Searchcity).send_keys(Keys.ENTER)
        #chwd = self.driver.window_handles
        #self.driver.switch_to.window(chwd)
        time.sleep(5)
        text1=self.driver.find_element(*WeatherPage.TemperatureSearch).text
        print(text1)
        return text1






