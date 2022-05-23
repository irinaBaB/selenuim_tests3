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
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.tot.wd
        self.open_groups_page()
        wd.find_element(By.NAME,"selected[]").click()
        wd.find_element(By.NAME,"delete").click()
        self.return_to_groups_page()

    def edit_first_group(self,group):
        wd = self.tot.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME,"edit").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()




    def open_groups_page(self):
        wd = self.tot.wd
        wd.find_element(By.LINK_TEXT, 'groups').click()