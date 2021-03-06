from model.details import Details


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Details(firstname="first name", middlename="test del"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
