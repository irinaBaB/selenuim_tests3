# -*- coding: utf-8 -*-
from models.group_base import Group


def test_add_group(app):
    app.group.create(Group(name="alla", header="modified", footer="mamont"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

def test_add_group_with_limited_fields(app):
    app.group.create(Group(name="fff"))



...



