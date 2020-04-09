# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test name", header="test header", footer="test footer"))
    # logout to ensure that fixture validation works as intended
    app.session.logout()


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
