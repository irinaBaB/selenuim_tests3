# -*- coding: utf-8 -*-
from models.group_base import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="alla", header="modified", footer="mamont"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()




