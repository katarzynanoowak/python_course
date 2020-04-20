from sys import maxsize


class Details:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address1=None, telhome=None, mobile=None, telwork=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, address2=None, telhome2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address1 = address1
        self.telhome = telhome
        self.mobile = mobile
        self.telwork = telwork
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.telhome2 = telhome2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname == other.lastname or
                                                                                 self.lastname is None or
                                                                                 other.lastname is None or
                                                                                 self.firstname is None or
                                                                                 self.firstname == other.firstname or
                                                                                 other.firstname is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
