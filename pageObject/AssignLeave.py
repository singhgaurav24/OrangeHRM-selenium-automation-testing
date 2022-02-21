from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AssignLeave:

    assign_leave_btn_Text = "Assign Leave"

    emp_name_textbox_XPATH = '//*[@id="assignleave_txtEmployee_empName"]'
    leave_type_dropdown_id = "assignleave_txtLeaveType"
    leave_balance_xpath = '//*[@id="assignleave_leaveBalance"]'
    from_date_field_id = "assignleave_txtFromDate"
    to_date_field_id = "assignleave_txtToDate"
    comment_textbox_id = "assignleave_txtComment"
    cnf_btn_id = "confirmOkButton"

    assign_btn_id = '//*[@id="assignBtn"]'

    def __init__(self, driver):
        self.driver = driver

    def clickAssignLeave(self):
        self.driver.find_element(By.LINK_TEXT, self.assign_leave_btn_Text).click()

    def setEmpName(self, empName):
        self.driver.find_element(By.XPATH, self.emp_name_textbox_XPATH).clear()
        self.driver.find_element(By.XPATH, self.emp_name_textbox_XPATH).send_keys(empName)

    def setLeaveType(self, leaveTypeValue):
        var = Select(self.driver.find_element(By.ID, self.leave_type_dropdown_id))
        var.select_by_value(leaveTypeValue)

    def setFromDate(self, fromDate):
        self.driver.find_element(By.ID, self.from_date_field_id).clear()
        self.driver.find_element(By.ID, self.from_date_field_id).send_keys(fromDate)

    def setToDate(self, toDate):
        self.driver.find_element(By.ID, self.to_date_field_id).clear()
        self.driver.find_element(By.ID, self.to_date_field_id).send_keys(toDate)

    def setComment(self, comment):
        self.driver.find_element(By.ID, self.comment_textbox_id).clear()
        self.driver.find_element(By.ID, self.comment_textbox_id).send_keys(comment)

    def clickAssign(self):
        self.driver.find_element(By.XPATH, self.assign_btn_id).click()

    def clickCnfBtn(self):
        self.driver.find_element(By.ID, self.cnf_btn_id).click()




