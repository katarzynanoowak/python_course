from model.details import Details


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Details(firstname="something", middlename="to", lastname="modify", nickname="test3"))
    old_contacts = app.contact.get_contact_list()
    contact = Details(firstname="modified", middlename="test3")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(new_contacts, key=Details.id_or_max)
