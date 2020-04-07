class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # added delete_all_cookies() to ensure that tests can run altogether in the same session
        wd.delete_all_cookies()
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='LOGIN']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("LOGOUT").click()
