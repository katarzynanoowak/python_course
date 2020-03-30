# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
            wd.get("http://localhost/addressbook/addressbook/group.php")

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        # log in
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='LOGIN']").click()
        # open group page
        wd.find_element_by_link_text("GROUPS").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").send_keys("test name")
        wd.find_element_by_name("group_header").send_keys("test header")
        wd.find_element_by_name("group_footer").send_keys("test footer")
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        wd.find_element_by_link_text("group page").click()
        # logout
        wd.find_element_by_link_text("LOGOUT").click()



    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
