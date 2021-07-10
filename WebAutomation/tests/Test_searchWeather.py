from testData.testdatanotepad import testdatanotepad
from Utilities.BaseClass import BaseClass
from PageObjects.WeatherPage import WeatherPage
from testData import testdatanotepad
import pytest
import time

class Testcase(BaseClass):

    def test_weather(self):
        city=testdatanotepad.testdatanotepad.Dict
        print(city)
        cities = city['City']
        Dict1=[]

        for ci in cities:
            print(ci)
            homepage=WeatherPage(self.driver)
            time.sleep(5)
            temp =homepage.ActionSearchcity(ci)
            Dict1.append(temp)
            print(Dict1)
            time.sleep(5)





