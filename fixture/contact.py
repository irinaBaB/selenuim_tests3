from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self,tot):
        self.tot=tot

    def return_to_home_page(self):
        wd = self.tot.wd
        wd.get("http://localhost:8081/addressbook/")
        wd.find_element(By.LINK_TEXT, "home").click()
        wd.find_element(By.ID, "container").click()

    def create(self, contact):
        wd = self.tot.wd
        self.open_contact_page()
        self.fill_contact_form(contact)

        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.tot.wd
        self.return_to_home_page()
        self.select_first_contact()
        wd.find_element(By.XPATH,"//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element(By.LINK_TEXT, "home").click()
        self.return_to_home_page()

    def edit_first_contact(self,contact):
        wd = self.tot.wd
        self.return_to_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element(By.XPATH,"//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()

    def fill_contact_form(self,details):
        self.contact_type_field(contact_text='firstname',field_name= details.firstname)
        self.contact_type_field(contact_text='lastname', field_name=details.lastname)
        self.contact_type_field(contact_text='nickname', field_name=details.nickname)
        self.contact_type_field(contact_text='title', field_name=details.title)
        self.contact_type_field(contact_text='company', field_name=details.companyname)
        self.contact_type_field(contact_text='address', field_name=details.address)
        self.contact_type_field(contact_text='work', field_name=details.workphone)
        self.contact_type_field(contact_text='email', field_name=details.email)
        self.contact_type_field(contact_text='bday', field_name=details.birthday)
        self.contact_type_field(contact_text='bmonth', field_name=details.bmonth)
        self.contact_type_field(contact_text='byear', field_name=details.byear)


    def contact_type_field(self, contact_text,field_name):
        wd = self.tot.wd
        if contact_text not in ["bday","bmonth"] and field_name is not None:
            wd.find_element(By.NAME, contact_text).click()
            wd.find_element(By.NAME, contact_text).clear()
            wd.find_element(By.NAME, contact_text).send_keys(field_name)
        elif contact_text in ["bday","bmonth"] and field_name is not None:
            wd.find_element(By.NAME, contact_text).click()
            Select(wd.find_element(By.NAME, contact_text)).select_by_visible_text(field_name)

    def select_first_contact(self):
        wd = self.tot.wd
        wd.find_element(By.NAME, "selected[]").click()

    def open_contact_page(self):
        wd = self.tot.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        #wd.get("http://localhost:8081/addressbook/edit.php")

    def  count(self):
        wd = self.tot.wd
        return len(wd.find_elements(By.NAME, "selected[]"))