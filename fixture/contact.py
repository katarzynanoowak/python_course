from selenium.webdriver.support.ui import Select
import random
from model.myrandomdata import MyData
from model.details import Details
import re
from selenium.webdriver.common.keys import Keys


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
        # wd.find_element_by_xpath("//option[@value='[none]']").click()
        wd.find_element_by_xpath("//option[@value='284']").click()

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
        self.select_contact_by_index(0)

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
        wd.find_elements_by_xpath('//img[@alt="EDIT"]')[index].click()

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
            for row in wd.find_elements_by_name("entry"):
                cell = row.find_elements_by_tag_name("td")
                text_lastname = cell[1].text
                text_firstname = cell[2].text
                id_contact = cell[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cell[5].text
                all_emails = cell[4].text
                text_address = cell[3].text
                self.contact_cache.append(Details(lastname=text_lastname, firstname=text_firstname, id=id_contact,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address1=text_address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        telhome = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        telwork = wd.find_element_by_name("work").get_attribute("value")
        telhome2 = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address1 = wd.find_element_by_name("address").get_attribute("value")
        return Details(firstname=firstname, lastname=lastname, id=id, telhome=telhome, mobile=mobile, telwork=telwork,
                       telhome2=telhome2, email1=email1, email2=email2, email3=email3, address1=address1)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        telhome = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        telwork = re.search("W: (.*)", text).group(1)
        telhome2 = re.search("P: (.*)", text).group(1)
        return Details(telhome=telhome, mobile=mobile, telwork=telwork, telhome2=telhome2)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//img[@alt="EDIT"]').click()
        self.fill_contact_form(new_contact_data)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('input[value="DELETE"]').click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def add_contact_to_group(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('select[name="to_group"]').click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[4]/select/option[19]").click()
        # wd.find_element_by_css_selector('option[value="300"]').click()
        wd.find_element_by_css_selector('input[name="add"]').click()

    def delete_contact_from_group(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_css_selector('select[name="group"]').click()
        wd.find_element_by_css_selector('option[value="300"]').click()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('input[name="remove"]').click()
