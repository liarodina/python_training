import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_value("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        # init contact creation
        self.open_add_new_page()
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("home", contact.home)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_add_new_page(self):
        # open add new page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        #wd.find_element_by_name("Delete").click()
        time.sleep(0.1)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@title='Edit'])").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("edit")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='update'])").click()
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@title='Edit'])").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))


