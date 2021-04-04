from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test_not_any_contact"))
    app.contact.delete_first_contact()

