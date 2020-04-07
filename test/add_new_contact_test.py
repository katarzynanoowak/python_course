# -*- coding: utf-8 -*-
from model.details import Details
import random
from model.myrandomdata import MyData


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Details(firstname="first name", middlename=random.choice(MyData.name),
                               lastname=random.choice(MyData.lastname), nickname=random.choice(MyData.nickname),
                               title="tilte", company="company", address1="address1",
                               telhome=random.choice(MyData.phone), mobile=random.choice(MyData.phone),
                               telwork=random.choice(MyData.phone), fax=random.choice(MyData.phone),
                               email1=random.choice(MyData.email), email2=random.choice(MyData.email),
                               email3=random.choice(MyData.email), homepage="www.homepage.com",
                               address2="address2", telhome2=random.choice(MyData.phone), notes="notes"))
    app.session.logout()
