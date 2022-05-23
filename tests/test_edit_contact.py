from models.contact_base import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="kunya", lastname="Saschik", title="hubby", companyname="winsome street",
                               nickname="fgfgfgf", address="2/4 finland street", workphone="0927689",
                               email="izir@gmail.com", birthday="3", bmonth="April", byear="1973"))
    app.session.logout()