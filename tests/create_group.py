# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from models.group_base import Group

@pytest.fixture
def app(request):
    fixture= Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="alla", header="modified", footer="mamont"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


