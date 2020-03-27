# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/group.php")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='LOGIN']").click()
        wd.find_element_by_link_text("GROUPS").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys("test name")
        wd.find_element_by_name("group_header").send_keys("test header")
        wd.find_element_by_name("group_footer").send_keys("test footer")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("LOGOUT").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
