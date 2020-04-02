# -*- coding: utf-8 -*-
import pytest
from model_contact.details import Details
import random
from model_contact.myrandomdata import MyData
from fixture_contact.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Details(firstname="first name", middlename=random.choice(MyData.name),
                                    lastname=random.choice(MyData.lastname), nickname=random.choice(MyData.nickname),
                                    title="tilte", company="company", address1="address1",
                                    telhome=random.choice(MyData.phone), mobile=random.choice(MyData.phone),
                                    telwork=random.choice(MyData.phone), fax=random.choice(MyData.phone),
                                    email1=random.choice(MyData.email), email2=random.choice(MyData.email),
                                    email3=random.choice(MyData.email), homepage="www.homepage.com",
                                    address2="address2", telhome2=random.choice(MyData.phone), notes="notes"))
    app.logout()