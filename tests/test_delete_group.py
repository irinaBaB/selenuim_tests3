from models.group_base import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="fofka"))
    app.group.delete_first_group()