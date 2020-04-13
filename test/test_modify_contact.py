from model.details import Details


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Details(firstname="something", middlename="to", lastname="modify", nickname="test3"))
    app.contact.modify_first_contact(Details(firstname="modified", middlename="test3"))

