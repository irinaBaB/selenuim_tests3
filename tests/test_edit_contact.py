from models.contact_base import Contact


def test_edit_first_contact_details1(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="kunya", lastname="Saschik", title="hubby", companyname="winsome street"))
    app.session.logout()


def test_edit_first_contact_only_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="paramount", lastname="Slava"))
    app.session.logout()

def test_edit_first_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(address="new adress", workphone="17171755558888"))
    app.session.logout()