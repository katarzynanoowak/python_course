from model.details import Details
import random
from model.group import Group
from fixture.orm import ORMFixture

dba = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group_list = db.get_group_list()
    group = random.choice(group_list)
    contact_list = dba.get_contacts_in_group(Group(id=group.id))
    if len(contact_list) == 0:
        app.contact.create(Details(firstname="firstname", middlename="middlename", lastname="test", nickname="test"))
    contact = random.choice(contact_list)
    app.contact.delete_contact_from_group(contact.id, group.id)
    new_contact_list = list(dba.get_contacts_in_group(Group(id=group.id)))
    assert contact not in new_contact_list
