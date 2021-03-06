from model.details import Details
import random
from model.myrandomdata import MyData


def test_edit_first(app):
    app.contact.edit_first(Details(firstname="edited name", middlename=random.choice(MyData.name),
                                   lastname=random.choice(MyData.lastname), nickname=random.choice(MyData.nickname),
                                   title=" edited title", company="edited company", address1="edited address1",
                                   telhome=random.choice(MyData.phone), mobile=random.choice(MyData.phone),
                                   telwork=random.choice(MyData.phone), fax=random.choice(MyData.phone),
                                   email1=random.choice(MyData.email), email2=random.choice(MyData.email),
                                   email3=random.choice(MyData.email), homepage="www.homepage edited.com",
                                   address2="address edited", telhome2=random.choice(MyData.phone),
                                   notes="edited notes"))


