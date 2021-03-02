from model.group import Group


def test_delete_first_group(app):
   app.session.login(username="admin", password="secret")
   app.group.delete_first_group() (Group(name="qqq", header="qqq", footer="qqq"))
   app.session.logout()

