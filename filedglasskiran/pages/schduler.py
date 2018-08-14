import schedule
import time
from selenium import webdriver
import schduler
from pages.login_page import LoginPage
from pages.timesheet import TimeSheet
from selenium.webdriver.common.by import By

class schdulePage():

    def job():
        baseurl = 'https://www.fieldglass.net'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)

        lp = LoginPage(driver)
        lp.login('kiranreddy35', 'kpsskkr1473')

        userAcount = driver.find_element(By.XPATH, '//*[@id="activelinkedUserName"]')
        if userAcount is not None:
            print('login successful')
        else:
            print('log in failed')

        lp1=TimeSheet(driver)
        lp1.TimeSheetPage()

        driver.close()

    print("I'm working...")
    schedule.every().day.at("12:13").do(job)

#    schedule.every(1).minutes.do(job)
#    schedule.every().hour.do(job)
#    schedule.every().monday.do(job)
#    schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


tt=schdulePage()
tt.job()
