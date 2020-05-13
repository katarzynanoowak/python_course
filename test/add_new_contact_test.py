# -*- coding: utf-8 -*-
from model.details import Details


def test_add_new_contact(app, json_contacts, db, check_ui):
    details = json_contacts
    old_contacts = db.get_contact_list()
    contacts_on_hp = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(contacts_on_hp, key=Details.id_or_max)
    app.contact.create(details)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(details)
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(new_contacts, key=Details.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Details.id_or_max) == sorted(app.contact.get_contact_list(), key=Details.id_or_max)
