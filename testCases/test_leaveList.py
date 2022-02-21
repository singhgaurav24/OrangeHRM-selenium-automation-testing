# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from pageObject.baseFile import BaseFile
#
#
# class Test_003_LeaveList:
#
#     def test_leaveList(self, setup):
#         self.driver = setup
#         self.bF = BaseFile(self.driver)
#         self.bF.fillLoginPage()
#
#         self.bF.fillLeaveList()
#         self.driver.close()
#
#         output = self.driver.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td').text
#         if output == "No Records Found":
#             assert True
#             self.driver.close()
#         else:
#             # self.driver.save_screenshot(".\\Screenshorts\\" + "test_assignLeave.png")
#             self.driver.close()
#             assert False
