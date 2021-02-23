
# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


# функция инициализации фикстру
# пометка для pytest
@pytest.fixture
def app(request):
   # создаем фикстуру = объект типа application
   fixture = Application()
   request.addfinalizer(fixture.destroy)
   # верни фикструру
   return fixture


# в качестве параметра(был self) принимаем  fixture = Application()
def test_add_group(app):
   app.login(username="admin", password="secret")
   app.create_group(Group(name="qqq", header="qqq", footer="qqq"))
   app.logout()


def test_add_empty_group(app):
   app.login(username="admin", password="secret")
   app.create_group(Group(name="", header="", footer=""))
   app.logout()
