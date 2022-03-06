import pytest
from selenium import webdriver

from pageObject.LeaveList import LeaveList
from pageObject.LoginPage import LoginPage
from utlities.readProperties import ReadConfig
from pageObject.AssignLeave import AssignLeave


class BaseFile:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    empName = ReadConfig.getEmpName()
    leaveTypeValue = ReadConfig.getLeaveTypeValue()
    fromDate = ReadConfig.getFromDate()
    toDate = ReadConfig.getToDate()
    comment = ReadConfig.getComment()

    # empName = ReadConfig.getEmpName()
    # fromDate = ReadConfig.getFromDate()
    # toDate = ReadConfig.getToDate()
    value = ReadConfig.getValue()

    def __init__(self, driver):
        self.driver = driver
        self.aL = None
        self.lp = None
        self.lL = None

    def fillLoginPage(self):
#         self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        return self.lp.clickLogin()

    def fillAssignLeave(self):
        self.aL = AssignLeave(self.driver)
        self.aL.clickAssignLeave()
        self.aL.setEmpName(self.empName)
        self.aL.setLeaveType(self.leaveTypeValue)
        self.aL.setFromDate(self.fromDate)
        self.aL.setToDate(self.toDate)
        self.aL.setComment(self.comment)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        return self.aL.clickAssign()

    def fillLeaveList(self):
        self.lL = LeaveList(self.driver)
        self.lL.clickLeaveList()
        self.lL.setFromDate(self.fromDate)
        self.lL.setToDate(self.toDate)
        self.lL.setSelectStatus()
        self.lL.setEmpName(self.empName)
        self.lL.setSubUnit()
        return self.lL.clickSearch()




