from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self,tot):
        self.tot=tot

    def return_to_groups_page(self):
        wd = self.tot.wd
        wd.find_element(By.LINK_TEXT, "group page").click()
        wd.find_element(By.XPATH, "//form[@action='/addressbook/group.php']").click()

    def create(self, group):
        wd = self.tot.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.tot.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME,"delete").click()
        self.return_to_groups_page()

    def edit_first_group(self,new_group_data):
        wd = self.tot.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME,"edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        self.group_type_field(text='group_name',field_name=group.name)
        self.group_type_field(text='group_header', field_name=group.header)
        self.group_type_field(text='group_footer', field_name=group.footer)

    def group_type_field(self,text,field_name):
        wd = self.tot.wd
        if field_name is not None:
            wd.find_element(By.NAME,text).click()
            wd.find_element(By.NAME,text).clear()
            wd.find_element(By.NAME,text).send_keys(field_name)

    def select_first_group(self):
        wd = self.tot.wd
        wd.find_element(By.NAME, "selected[]").click()

    def open_groups_page(self):
        wd = self.tot.wd
        wd.find_element(By.LINK_TEXT, 'groups').click()