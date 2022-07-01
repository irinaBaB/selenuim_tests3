from models.contact_base import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='todelete',lastname='bob'))
    app.contact.delete_first_contact()