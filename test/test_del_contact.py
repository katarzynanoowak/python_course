from model.details import Details
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Details(firstname="first name", middlename="test del"))
    old_contacts = db.get_contact_list()
    contacts_on_hp = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(contacts_on_hp, key=Details.id_or_max)
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Details.id_or_max) == sorted(app.contact.get_contact_list(), key=Details.id_or_max)
