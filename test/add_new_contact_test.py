# -*- coding: utf-8 -*-
from model.details import Details


def test_add_new_contact(app, json_contacts):
    details = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(details)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(details)
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(new_contacts, key=Details.id_or_max)

