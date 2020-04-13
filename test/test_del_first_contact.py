from model.details import Details


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Details(firstname="first name", middlename="test del"))
    app.contact.delete_first_contact()

