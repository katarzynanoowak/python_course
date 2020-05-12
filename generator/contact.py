from model.details import Details
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*50
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number():
    digits = string.digits
    return "".join([random.choice(digits) for i in range(10)])


def random_email(prefix, maxlen):
    symbols_em = string.ascii_letters + "@"*100 + string.digits
    return prefix + "".join([random.choice(symbols_em) for i in range(random.randrange(maxlen))])


testdata = [Details(firstname="", middlename="", lastname="", nickname="", title="", company="", address1="", telhome="",
                    mobile="", telwork="", fax="", email1="", email2="", email3="", homepage="", address2="", telhome2="",
                    notes="")] + [
    Details(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 10), title=random_string("title", 20),
            company=random_string("company", 20), address1=random_string("address1", 30), telhome=random_number(),
            mobile=random_number(), telwork=random_number(), fax=random_number(), email1=random_email("email1", 15),
            email2=random_email("", 15), email3=random_email("", 15), homepage=random_string("homepage", 14),
            address2=random_string("address2", 30), telhome2=random_number(), notes=random_string("notes", 30))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
