from selenium.webdriver.support.ui import Select
import random
from model.myrandomdata import MyData
from model.details import Details


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
        self.fill_contact_form(details)
        self.submit()
        self.return_to_homepage()
        self.contact_cache = None

    def fill_contact_form(self, details):
        wd = self.app.wd
        self.change_field_value("firstname", details.firstname)
        self.change_field_value("middlename", details.middlename)
        self.change_field_value("lastname", details.lastname)
        self.change_field_value("nickname", details.nickname)
        self.change_field_value("title", details.title)
        self.change_field_value("company", details.company)
        self.change_field_value("address", details.address1)
        self.change_field_value("home", details.telhome)
        self.change_field_value("mobile", details.mobile)
        self.change_field_value("work", details.telwork)
        self.change_field_value("fax", details.fax)
        self.change_field_value("email", details.email1)
        self.change_field_value("email2", details.email2)
        self.change_field_value("email3", details.email3)
        self.change_field_value("homepage", details.homepage)
        self.change_field_value("address2", details.address2)
        self.change_field_value("phone2", details.telhome2)
        self.change_field_value("notes", details.notes)

    def upload_photo(self):
        wd = self.app.wd
        elm = wd.find_element_by_name("photo")
        elm.send_keys("C:\\Users\\katarzyna.nowak\\Desktop\\cat.png")

    def upload_new_photo(self):
        wd = self.app.wd
        elm = wd.find_element_by_name("photo")
        elm.send_keys("C:\\Users\\katarzyna.nowak\\Desktop\\cone.png")

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

    def edit_dates(self):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(random.choice(MyData.day))
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(random.choice(MyData.month))
        wd.find_element_by_name("byear").send_keys(random.choice(MyData.year))
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(random.choice(MyData.day))
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(random.choice(MyData.amonth))
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

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and wd.find_element_by_id("MassCB").is_displayed):
            wd.get("http://localhost/addressbook/addressbook/")

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='EDIT']").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='EDIT']")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.text
                id_contact = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Details(lastname=text, id=id_contact))
        return list(self.contact_cache)
