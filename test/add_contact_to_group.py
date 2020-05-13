from model.details import Details
import random
from model.group import Group
from fixture.orm import ORMFixture


dba = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Details(firstname="firstname", middlename="middlename", lastname="test", nickname="test"))
    old_contacts = db.get_contact_list()
    contacts_on_hp = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Details.id_or_max) == sorted(contacts_on_hp, key=Details.id_or_max)
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group(contact.id)
    l = list(dba.get_contacts_in_group(Group(id="300")))
    assert contact in l

