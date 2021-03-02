# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="test", middlename="test", nickname="test", home="432112", email="test@mail.com"))
    app.session.logout()
