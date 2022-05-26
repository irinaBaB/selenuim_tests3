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
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.companyname)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.workphone)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.birthday)
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.tot.wd
        self.select_first_contact()
        wd.find_element(By.XPATH,"//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def edit_first_contact(self,contact):
        wd = self.tot.wd
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
        if field_name is not None:
            wd.find_element(By.NAME, contact_text).click()
            wd.find_element(By.NAME, contact_text).clear()
            wd.find_element(By.NAME, contact_text).send_keys(field_name)

    def select_first_contact(self):
        wd = self.tot.wd
        wd.find_element(By.NAME, "selected[]").click()

    def open_contact_page(self):
        wd = self.tot.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.get("http://localhost:8081/addressbook/edit.php")