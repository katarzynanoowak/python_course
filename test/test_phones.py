import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(2)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(2)
    assert contact_from_view_page.telhome == contact_from_edit_page.telhome
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.telwork == contact_from_edit_page.telwork
    assert contact_from_view_page.telhome2 == contact_from_edit_page.telhome2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.telhome, contact.mobile,
                                                                               contact.telwork, contact.telhome2]))))
