import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")
# config.read("/home/gaurav/PycharmProjects/OrangeHRM-selenium-automation-testing-master/Configurations/config.ini")
# config.read(r"C:\Users\DELL\selenium_work\OrangeHRM-selenium-automation-testing\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getEmpName():
        empName = config.get('Assign Leave', 'empName')
        return empName

    @staticmethod
    def getLeaveTypeValue():
        leaveTypeValue = config.get('Assign Leave', 'leaveTypeValue')
        return leaveTypeValue

    @staticmethod
    def getFromDate():
        fromDate = config.get('Assign Leave', 'fromDate')
        return fromDate

    @staticmethod
    def getToDate():
        toDate = config.get('Assign Leave', 'toDate')
        return toDate

    @staticmethod
    def getComment():
        comment = config.get('Assign Leave', 'comment')
        return comment

    @staticmethod
    def getValue():
        value = config.get('Leave List', 'value')
        return value

