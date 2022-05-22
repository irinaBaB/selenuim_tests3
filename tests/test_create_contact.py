# -*- coding: utf-8 -*-
from models.contact_base import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="lola", lastname="poni", title="mr", companyname="cola",
                               nickname="fgfgfgf", address="2/4 finland street", workphone="0927689",
                               email="izir@gmail.com", birthday="3", bmonth="April", byear="1973"))
    app.session.logout()






