# -*- coding: utf-8 -*-
from model.details import Details
import random
from model.myrandomdata import MyData


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Details(firstname="first name", middlename=random.choice(MyData.name),
                               lastname=random.choice(MyData.lastname), nickname=random.choice(MyData.nickname),
                               title="title", company="company", address1="address1",
                               telhome=random.choice(MyData.phone), mobile=random.choice(MyData.phone),
                               telwork=random.choice(MyData.phone), fax=random.choice(MyData.phone),
                               email1=random.choice(MyData.email), email2=random.choice(MyData.email),
                               email3=random.choice(MyData.email), homepage="www.homepage.com",
                               address2="address2", telhome2=random.choice(MyData.phone), notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(new_contacts, key=Details.id_or_max)

