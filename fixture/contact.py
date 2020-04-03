from selenium.webdriver.support.ui import Select
import random
from model.myrandomdata import MyData


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("ADD_NEW").click()

    def create(self, details):
        wd = self.app.wd
        self.open_add_new()
        self.upload_photo()
        self.set_dates()
        self.select_group()
        wd.find_element_by_name("firstname").send_keys(details.firstname)
        wd.find_element_by_name("middlename").send_keys(details.middlename)
        wd.find_element_by_name("lastname").send_keys(details.lastname)
        wd.find_element_by_name("nickname").send_keys(details.nickname)
        wd.find_element_by_name("title").send_keys(details.title)
        wd.find_element_by_name("company").send_keys(details.company)
        wd.find_element_by_name("address").send_keys(details.address1)
        wd.find_element_by_name("home").send_keys(details.telhome)
        wd.find_element_by_name("mobile").send_keys(details.mobile)
        wd.find_element_by_name("work").send_keys(details.telwork)
        wd.find_element_by_name("fax").send_keys(details.fax)
        wd.find_element_by_name("email").send_keys(details.email1)
        wd.find_element_by_name("email2").send_keys(details.email2)
        wd.find_element_by_name("email3").send_keys(details.email3)
        wd.find_element_by_name("homepage").send_keys(details.homepage)
        wd.find_element_by_name("address2").send_keys(details.address2)
        wd.find_element_by_name("phone2").send_keys(details.telhome2)
        wd.find_element_by_name("notes").send_keys(details.notes)
        self.submit()
        self.return_to_homepage()

    def upload_photo(self):
        wd = self.app.wd
        elm = wd.find_element_by_name("photo")
        elm.send_keys("C:\\Users\\katarzyna.nowak\\Desktop\\cat.png")

    def set_dates(self):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(random.choice(MyData.day))
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(random.choice(MyData.month))
        wd.find_element_by_name("byear").send_keys(random.choice(MyData.year))
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(random.choice(MyData.day))
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(random.choice(MyData.month))
        wd.find_element_by_name("ayear").send_keys(random.choice(MyData.year))

    def select_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()