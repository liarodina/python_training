# главный класс фикстуры
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        # помошник получает ссылку на объект класса Application
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
