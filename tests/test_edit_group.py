from models.group_base import Group

def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="trusyi"))

def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="edited group", footer="test 1234567"))