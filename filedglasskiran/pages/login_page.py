from selenium.webdriver.common.by import By
import time

class LoginPage():
    def __init__(self, driver):
        self.driver =driver
    #locator

    _emailField='//*[@id="usernameId_new"]'
    _passwordField='//*[@id="passwordId_new"]'
    _loginButton='action'

    def getEmailField(self):
        return self.driver.find_element(By.XPATH, self._emailField)
    def getPassswordField(self):
        return self.driver.find_element(By.XPATH, self._passwordField)
    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._loginButton)

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)
    def enterPassword(self,password):
        self.getPassswordField().send_keys(password)
    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email,password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

