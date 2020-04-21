from model.details import Details
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Details(firstname="something", middlename="to", lastname="modify", nickname="test3"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Details(firstname="modified", middlename="test3")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(new_contacts, key=Details.id_or_max)
