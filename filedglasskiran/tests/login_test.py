from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.timesheet import TimeSheet
from selenium.common.exceptions import NoSuchElementException

import time

class LogInTest():
    def test_validLogin(self):
        baseurl = 'https://www.fieldglass.net'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)

        lp=LoginPage(driver)
        lp.login('kiranreddy35','kpsskkr1473')

        time.sleep(2)

        userAcount = driver.find_element(By.XPATH,'//*[@id="activelinkedUserName"]')
        if userAcount is not None:
            print('login successful')
        else:
            print('log in failed')

        lp1=TimeSheet(driver)
        lp1.TimeSheetPage()

ff=LogInTest()
ff.test_validLogin()