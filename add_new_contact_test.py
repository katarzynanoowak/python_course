# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from primarydetails import PrimaryDetails
from secondarydetails import SecondaryDetails
import random
from myrandomdata import MyData


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_page(self, wd):
        wd.get("http://localhost/addressbook/addressbook/group.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='LOGIN']").click()

    def open_add_new(self, wd):
        wd.find_element_by_link_text("ADD_NEW").click()

    def fill_primary_details(self, wd, primarydetails):
        wd.find_element_by_name("firstname").send_keys(primarydetails.firstname)
        wd.find_element_by_name("middlename").send_keys(primarydetails.middlename)
        wd.find_element_by_name("lastname").send_keys(primarydetails.lastname)
        wd.find_element_by_name("nickname").send_keys(primarydetails.nickname)
        wd.find_element_by_name("title").send_keys(primarydetails.title)
        wd.find_element_by_name("company").send_keys(primarydetails.company)
        wd.find_element_by_name("address").send_keys(primarydetails.address1)
        wd.find_element_by_name("home").send_keys(primarydetails.telhome)
        wd.find_element_by_name("mobile").send_keys(primarydetails.mobile)
        wd.find_element_by_name("work").send_keys(primarydetails.telwork)
        wd.find_element_by_name("fax").send_keys(primarydetails.fax)
        wd.find_element_by_name("email").send_keys(primarydetails.email1)
        wd.find_element_by_name("email2").send_keys(primarydetails.email2)
        wd.find_element_by_name("email3").send_keys(primarydetails.email3)
        wd.find_element_by_name("homepage").send_keys(primarydetails.homepage)

    def upload_photo(self, wd):
        elm = wd.find_element_by_name("photo")
        elm.send_keys("C:\\Users\\katarzyna.nowak\\Desktop\\cat.png")

    def fill_secondary_details(self, wd, secondarydetails):
        wd.find_element_by_name("address2").send_keys(secondarydetails.address2)
        wd.find_element_by_name("phone2").send_keys(secondarydetails.telhome2)
        wd.find_element_by_name("notes").send_keys(secondarydetails.notes)

    def set_birthday_date(self, wd):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(random.choice(MyData.day))
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(random.choice(MyData.month))
        wd.find_element_by_name("byear").send_keys(random.choice(MyData.year))

    def set_aniversary_date(self, wd):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(random.choice(MyData.day))
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(random.choice(MyData.month))
        wd.find_element_by_name("ayear").send_keys(random.choice(MyData.year))

    def select_group(self, wd):
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()

    def submit(self, wd):
            wd.find_element_by_name("submit").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("LOGOUT").click()

    def test_add_new_contact(self):
        wd = self.wd
        self.open_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new(wd)
        self.upload_photo(wd)
        self.fill_primary_details(wd, PrimaryDetails(firstname=random.choice(MyData.name),
                                                     middlename=random.choice(MyData.name),
                                                     lastname=random.choice(MyData.lastname),
                                                     nickname=random.choice(MyData.nickname), title="tilte",
                                                     company="company", address1="address1",
                                                     telhome=random.choice(MyData.phone),
                                                     mobile=random.choice(MyData.phone),
                                                     telwork=random.choice(MyData.phone),
                                                     fax=random.choice(MyData.phone),
                                                     email1=random.choice(MyData.email),
                                                     email2=random.choice(MyData.email),
                                                     email3=random.choice(MyData.email), homepage="www.homepage.com"))
        self.set_birthday_date(wd)
        self.set_aniversary_date(wd)
        self.select_group(wd)
        self.fill_secondary_details(wd, SecondaryDetails(address2="address2", telhome2=random.choice(MyData.phone),
                                                         notes="notes"))
        self.submit(wd)
        self.return_to_homepage(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
