from model.details import Details
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Details(firstname="something", middlename="to", lastname="modify", nickname="test3"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, Details(firstname="modified", middlename="test3"))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Details.id_or_max) == sorted(app.contact.get_contact_list(), key=Details.id_or_max)
