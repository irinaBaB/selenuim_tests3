# -*- coding: utf-8 -*-
from models.contact_base import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="lola", lastname="poni", title="mr", companyname="cola",
                               nickname="fgfgfgf", address="2/4 finland street", workphone="0927689",
                               email="izir@gmail.com", birthday="3", bmonth="April", byear="1973"))

def test_add_contact_partly_filled(app):
    app.contact.create(Contact(firstname="lola", lastname="poni", title="mr", companyname="cola",nickname="fgfgfgf"))

def test_add_contact_with_empty_fields(app):
    app.contact.create(Contact(firstname="", lastname=""))


