# -*- coding: utf8 -*-
from zExceptions import BadRequest
from plone import api
from Products.Five.utilities.marker import mark,erase
from iol.utils.interfaces import IIolDocument
import logging


def _removePersistentUtility(portal):
    catalog = api.portal.get_tool('portal_catalog')
    brains = catalog(portal_type='PlominoDatabase')
    for brain in brains:
        db = brain.getObject()
        for doc in db.getAllDocuments():
            if IIolDocument.providedBy(doc):
                erase(doc,IIolDocument)


def uninstall(portal,reinstall=False):
    if not reinstall:
        setup_tool = portal.portal_setup
        _removePersistentUtility(portal)