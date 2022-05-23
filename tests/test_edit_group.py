from models.group_base import Group

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="matreshka", header="edited group", footer="test 1234567"))
    app.session.logout()