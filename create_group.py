# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from group_base import Group


class UnitTestsMineForever(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")

        self.open_groups_page(wd)
        self.create_group(wd, Group(name="alla", header="modified", footer="mamont"))

        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")

        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))

        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.XPATH, "//*/text()[normalize-space(.)='']/parent::*").click()

    def return_to_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "group page").click()
        wd.find_element(By.XPATH, "//form[@action='/addressbook/group.php']").click()

    def create_group(self, wd, group):
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()

    def open_groups_page(self, wd):
        wd.find_element(By.NAME, "new").click()

    def login(self, wd, username, password):
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(password)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8081/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
