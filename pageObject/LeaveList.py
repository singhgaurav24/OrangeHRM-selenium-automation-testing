from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LeaveList:
    leave_list_btn_Text = "Leave List"
    from_date_field_id = "calFromDate"
    to_date_field_id = "calToDate"
    show_leave_status_Xpath = '//*[@id="leaveList_chkSearchFilter_checkboxgroup_allcheck"]'
    emp_field_id = "leaveList_txtEmployee_empName"
    sub_unit_dropdown_id = "leaveList_cmbSubunit"
    past_emp_id = "leaveList_cmbWithTerminated"
    search_btn_id = "btnSearch"

    def __init__(self, driver):
        self.driver = driver

    def clickLeaveList(self):
        self.driver.find_element(By.LINK_TEXT, self.leave_list_btn_Text).click()

    def setFromDate(self, fromDate):
        self.driver.find_element(By.XPATH, self.from_date_field_id).clear()
        self.driver.find_element(By.XPATH, self.from_date_field_id).send_keys(fromDate)

    def setToDate(self, toDate):
        self.driver.find_element(By.XPATH, self.to_date_field_id).clear()
        self.driver.find_element(By.XPATH, self.to_date_field_id).send_keys(toDate)

    def setSelectStatus(self):
        # self.driver.find_element(By.XPATH, self.show_leave_status_Xpath).clear()
        self.driver.find_element(By.XPATH, self.show_leave_status_Xpath).click()

    def setEmpName(self, empName):
        self.driver.find_element(By.ID, self.emp_field_id).clear()
        self.driver.find_element(By.ID, self.emp_field_id).send_keys(empName)

    def setSubUnit(self, value):
        var = Select(self.driver.find_element(By.ID, self.sub_unit_dropdown_id))
        var.select_by_value(value)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.search_btn_id).click()




