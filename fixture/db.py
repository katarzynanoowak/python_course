import mysql.connector
from model.group import Group
from model.details import Details


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, notes, address2  from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address1, telhome, mobile, telwork, fax,
                 email1, email2, email3, homepage, notes, address2) = row
                list.append(Details(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, company=company, title=title, address1=address1, telhome=str(telhome),
                                    mobile=str(mobile), telwork=str(telwork), fax=str(fax), email1=email1, email2=email2,
                                    email3=email3, homepage=homepage, notes=notes, address2=address2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
