import pytest
from selenium import webdriver
from utlities.readProperties import ReadConfig
from pageObject.baseFile import BaseFile


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "OrangeHRM":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshorts\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.bF = BaseFile(self.driver)
        self.bF.fillLoginPage()

        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshorts\\" + "test_login.png")
            self.driver.close()
            assert False





