class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # added delete_all_cookies() to ensure that tests can run altogether in the same session
        # wd.delete_all_cookies()
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='LOGIN']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("LOGOUT").click()

    def ensure_logout(self):
        # wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("LOGOUT")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@id='top']/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        # wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
