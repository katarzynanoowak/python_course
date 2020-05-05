# -*- coding: utf-8 -*-
from model.details import Details
import pytest
from data.contacts import constant as testdata


@pytest.mark.parametrize("details", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, details):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(details)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(details)
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(new_contacts, key=Details.id_or_max)

