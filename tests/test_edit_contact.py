from models.contact_base import Contact


def test_edit_first_contact_details1(app):
    app.contact.edit_first_contact(Contact(firstname="kunya", lastname="Saschik", title="hubby", companyname="winsome street"))


def test_edit_first_contact_only_name(app):
    app.contact.edit_first_contact(Contact(firstname="paramount", lastname="Slava"))

def test_edit_first_contact_address(app):
    app.contact.edit_first_contact(Contact(address="new adress", workphone="17171755558888"))