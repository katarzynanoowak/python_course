from model.details import Details
import random
from model.group import Group
from fixture.orm import ORMFixture


dba = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Details(firstname="firstname", middlename="middlename", lastname="test", nickname="test"))
    old_contacts = db.get_contact_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = random.choice(old_contacts)
    group_list = db.get_group_list()
    group = random.choice(group_list)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_group_list = list(dba.get_contacts_in_group(Group(id=group.id)))
    assert contact in new_group_list


