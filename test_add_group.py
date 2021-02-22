# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from group import Group
from application import Application

#  функция инициализации фикстру
def app():



class TestAddGroup(unittest.TestCase):
    def setUp(self):
        # инициализация фикстуры
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="qqq", header="qqq", footer="qqq"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group( Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()



if __name__ == "__main__":
    unittest.main()
