from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self,tot):
        self.tot=tot

    def login(self,username, password):
        wd = self.tot.wd
        self.tot.open_home_page()
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(password)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.tot.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.XPATH, "//*/text()[normalize-space(.)='']/parent::*").click()

    def ensure_logout(self):
        wd = self.tot.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.tot.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self,username):
        wd = self.tot.wd
        return wd.find_element(By.XPATH,"//div[@id='top']/form/b").text == "("+username+")"


    def ensure_login(self,username,password):
        wd = self.tot.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)

