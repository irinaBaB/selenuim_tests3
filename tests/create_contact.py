# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from models.contact_base import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="lola", lastname="poni", title="mr", companyname="cola",
                               nickname="fgfgfgf", address="2/4 finland street", workphone="0927689",
                               email="izir@gmail.com", birthday="3", bmonth="April", byear="1973"))
    app.session.logout()




