# -*- coding: utf-8 -*-
from model.details import Details
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*50
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number():
    digits = string.digits
    return "".join([random.choice(digits) for i in range(10)])


def random_email(prefix, maxlen):
    symbols_em = string.ascii_letters + "@"*100 + string.digits
    return prefix + "".join([random.choice(symbols_em) for i in range(random.randrange(maxlen))])


testdata = [Details(firstname="", middlename="", lastname="", nickname="", title="", company="", address1="", telhome="",
                    mobile="", telwork="", fax="", email1="", email2="", email3="", homepage="", address2="", telhome2="",
                    notes="")] + [
    Details(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 10), title=random_string("title", 20),
            company=random_string("company", 20), address1=random_string("address1", 30), telhome=random_number(),
            mobile=random_number(), telwork=random_number(), fax=random_number(), email1=random_email("email1", 15),
            email2=random_email("", 15), email3=random_email("", 15), homepage=random_string("homepage", 14),
            address2=random_string("address2", 30), telhome2=random_number(), notes=random_string("notes", 30))
    for i in range(7)
]


@pytest.mark.parametrize("details", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, details):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(details)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(details)
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(new_contacts, key=Details.id_or_max)

