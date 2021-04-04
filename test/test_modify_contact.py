from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test_not_any_contact"))
    app.contact.modify_first_contact(Contact(firstname="new firstname"))


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test_not_any_contact"))
    app.contact.modify_first_contact(Contact(email="new email"))


