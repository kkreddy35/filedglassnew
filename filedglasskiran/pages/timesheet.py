from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

from tempora import schedule


class TimeSheet():
    def __init__(self, driver):
        self.driver =driver

    #locataor


    def TimeSheetPage(self):
        viewfield = '//*[@id="viewMenuTitle"]/figure/a/div'
        _time = 'viewMenu_2_timeSheet_link'
        _clickfromdate = '//*[@id="filterStartDate"]'
        _clickenddate = '//*[@id="filterEndDate"]'
        _selectstartmonth = 'month'
        _selectendmonth = 'month'
        _selectstartyear = 'year'
        _selectendyear = 'year'
        _viewicon = '//*[@id="timeSheet_supplier_list_visibility_1"]'
        _filterfield = '//*[@id="cSelForm"]/div[3]/input[2]'

        view_button = self.driver.find_element_by_xpath('//*[@id="viewMenuTitle"]/figure/a/div')
        view_button.click()
        time.sleep(1)

        timesheet = self.driver.find_element_by_id('viewMenu_2_timeSheet_link')
        timesheet.click()
        time.sleep(5)

        # To click on date
        clickfrom_date = self.driver.find_element_by_xpath('//*[@id="filterStartDate"]')
        clickfrom_date.click()
        time.sleep(2)

        # To Select start month
        select_month = Select(self.driver.find_element_by_name('month'))
        time.sleep(2)
        select_month.select_by_visible_text('March')
        time.sleep(2)
        ## select a year

        select_year = Select(self.driver.find_element_by_name('year'))
        time.sleep(2)
        select_year.select_by_value('2017')
        time.sleep(2)

        # Select a date
        a = self.driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr')
        for i in range(1, len(a)):
            j = self.driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr[%s]/td' % i)
            for st in j:
                if st.text.strip() == "10":
                    st.click()
                    break

        # to select end date
        clickend_date = self.driver.find_element_by_xpath('//*[@id="filterEndDate"]')
        clickend_date.click()

        ##select end month

        select_month = Select(self.driver.find_element_by_name('month'))
        time.sleep(2)
        select_month.select_by_visible_text('March')
        time.sleep(2)

        select_year = Select(self.driver.find_element_by_name('year'))
        time.sleep(2)
        select_year.select_by_value('2017')
        time.sleep(2)

        ##select end date
        b = self.driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr')
        for k in range(1, len(b)):
            l = self.driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr[%s]/td' % k)
            for et in l:
                if et.text.strip() == "20":
                    et.click()
                    break

        ##view button

        view1 = self.driver.find_element_by_xpath('//*[@id="timeSheet_supplier_list_visibility_1"]')
        view1.click()
        time.sleep(2)

        ##click filter

        filter_option = self.driver.find_element_by_xpath('//*[@id="cSelForm"]/div[3]/input[2]')
        filter_option.click()

        time.sleep(3)

#    schedule.every(1).minutes.do(job)


'''

class TimeSheet():

    def __init__(self, driver):
        self.driver = driver

    _viewfield = '//*[@id="viewMenuTitle"]/figure/a/div'
    _time= 'viewMenu_2_timeSheet_link'
    _clickfromdate = '//*[@id="filterStartDate"]'
    _clickenddate = '//*[@id="filterEndDate"]'
    _selectstartmonth = 'month'
    _selectendmonth = 'month'
    _selectstartyear = 'year'
    _selectendyear = 'year'



    def getViewfield(self):
        return self.driver.find_element(By.XPATH,self._viewfield)
    def getTimesheet(self):
        return self.driver.find_element(By.ID,self._time)
    def getFromDate(self):
        return self.driver.find_element(By.XPATH,self._clickfromdate)
    def getEndDate(self):
        return self.driver.find_element(By.XPATH, self._clickenddate)
    def getStsrtMonth(self):
        return self.driver.find_element(By.NAME,self._selectstartmonth)
    def getEndMonth(self):
        return self.driver.find_element(By.NAME,self._selectendmonth)
    def getStartYear(self):
        return self.driver.find_element(By.NAME,self._selectstartyear)
    def getEndYear(self):
        return self.driver.find_element(By.NAME,self._selectendyear)

    def clickview(self):
        self.getViewfield().click()
    def clicktimesheet(self):
        self.getTimesheet().click()
    def clickStartdate(self):
        self.getFromDate().click()
        a = driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr')
        for i in range(1, len(a)):
            j = driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr[%s]/td' % i)
            for st in j:
                if st.text.strip() == "10":
                    st.click()
                    break
    def selectStartmonth(self):
        self.getStsrtMonth().Select(select_by_visible_text('December'))

    def selectEnddate(self):
        self.getEndDate().click()
        b = driver.find_elements_(By.XPATH,'//*[@id="bottomCalFrame"]/div/table/tbody/tr')
        for k in range(1, len(b)):
            l = driver.find_elements(By.XPATH,'//*[@id="bottomCalFrame"]/div/table/tbody/tr[%s]/td' % k)
            for et in l:
                if et.text.strip() == "20":
                    et.click()
                    break
    def selectEndmonth(self):
        self.getEndMonth().Select(select_by_visible_text('March'))
    def selectStartyear(self):
        self.getStartYear().select_by_value('2017')

    def TimeSheetPage(self):
        self.clickview()
        self.clicktimesheet()
        self.clickStartdate()
        self.selectStartmonth()
        self.selectEnddate()
        self.selectEndmonth()
        self.selectStartyear()

'''

'''

class TimeSheet():
    def timesheettest(self):
        view = driver.find_element_by_xpath('//*[@id="viewMenuTitle"]/figure/a/div').click()
        time.sleep(1)

        timesheet = driver.find_element_by_id('viewMenu_2_timeSheet').click()
        time.sleep(5)

        # To click on date
        from_date = driver.find_element_by_xpath('//*[@id="filterStartDate"]')
        from_date.click()
        time.sleep(2)

        # To Select start month
        select = Select(driver.find_element_by_name('month'))
        time.sleep(2)
        select.select_by_visible_text('March')
        time.sleep(2)
        ## select a year

        select_year = Select(driver.find_element_by_name('year'))
        time.sleep(2)
        select_year.select_by_value('2017')
        time.sleep(2)

        # Select a date
        a = driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr')
        for i in range(1, len(a)):
            j = driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr[%s]/td' % i)
            for st in j:
                if st.text.strip() == "10":
                    st.click()
                    break

        # to select end date
        end_date = driver.find_element_by_xpath('//*[@id="filterEndDate"]')
        end_date.click()

        ##select end month

        select = Select(driver.find_element_by_name('month'))
        time.sleep(2)
        select.select_by_visible_text('March')
        time.sleep(2)

        ##select end date
        b = driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr')
        for k in range(1, len(b)):
            l = driver.find_elements_by_xpath('//*[@id="bottomCalFrame"]/div/table/tbody/tr[%s]/td' % k)
            for et in l:
                if et.text.strip() == "20":
                    et.click()
                    break

        ##view button

        view1 = driver.find_element_by_xpath('//*[@id="timeSheet_supplier_list_visibility_1"]')
        view1.click()
        time.sleep(2)
        ##click filter

        filter = driver.find_element_by_xpath('//*[@id="cSelForm"]/div[3]/input[2]').click()

        time.sleep(3)

        ##export

        xl = driver.find_element_by_xpath('//*[@id="download_timeSheet.supplier.list"]/span').click()
        time.sleep(3)
'''

