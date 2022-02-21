# import pytest
# from selenium import webdriver
# from pageObject.baseFile import BaseFile
# from selenium.webdriver.common.by import By
#
#
# class Test_002_AssignLeave:
#
#     def test_assignLeave(self, setup):
#         self.driver = setup
#         self.ld = BaseFile(self.driver)
#         self.ld.fillLoginPage()
#
#         self.ld.fillAssignLeave()
#         self.driver.close()
#
#         output = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/h1').text
#         if output == "Overlapping Leave Request Found":
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\Screenshorts\\" + "test_assignLeave.png")
#             self.driver.close()
#             assert False
