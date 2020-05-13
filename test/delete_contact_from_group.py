from model.details import Details
import random
from model.group import Group
from fixture.orm import ORMFixture

dba = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
    if len(dba.get_contacts_in_group(Group(id="300"))) == 0:
        app.contact.create(Details(firstname="firstname", middlename="middlename", lastname="test", nickname="test"))
    old_contacts = dba.get_contacts_in_group(Group(id="300"))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_from_group(contact.id)
    l = list(dba.get_contacts_in_group(Group(id="300")))
    assert contact not in l