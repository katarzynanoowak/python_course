# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/group.php")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='LOGIN']").click()
        wd.find_element_by_link_text("ADD_NEW").click()
        wd.find_element_by_name("firstname").send_keys("first name")
        wd.find_element_by_name("middlename").send_keys("middle name")
        wd.find_element_by_name("lastname").send_keys("lastname")
        wd.find_element_by_name("nickname").send_keys("nickname")
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys("C:\\fakepath\\a1.png")
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").send_keys("addres")
        wd.find_element_by_name("home").send_keys("12345678")
        wd.find_element_by_name("mobile").send_keys("123456789")
        wd.find_element_by_name("work").send_keys("12345678910")
        wd.find_element_by_name("fax").send_keys("12345678911")
        wd.find_element_by_name("email").send_keys("email@email.com")
        wd.find_element_by_name("email2").send_keys("email2@email.com")
        wd.find_element_by_name("email3").send_keys("email3@email.com")
        wd.find_element_by_name("homepage").send_keys("www.homepage.com")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("12")
        wd.find_element_by_xpath("//option[@value='12']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("MARCH")
        wd.find_element_by_xpath("//option[@value='March']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("18")
        wd.find_element_by_xpath("(//option[@value='18'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("DECEMBER")
        wd.find_element_by_xpath("(//option[@value='December'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2019")
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        wd.find_element_by_name("address2").send_keys("address2")
        wd.find_element_by_name("phone2").send_keys("987654321")
        wd.find_element_by_name("notes").send_keys("notes")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("LOGOUT").click()
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
