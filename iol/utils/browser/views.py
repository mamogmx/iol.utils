from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView
from plone import api

class getIolRoles(BrowserView):
    def __call__(self, *args, **kwargs):
        doc = self.aq_parent
        result = dict(
            iol_owner=[],
            iol_reviewer = [],
            iol_manager = [],
        )
        for usr,roles in doc.get_local_roles():
            if 'Owner' in roles:
                result['iol_owner'].append(usr)
            if 'iol-reviewer' in roles:
                result['iol_reviewer'].append(usr)
            if 'iol-manager' in roles:
                result['iol_manager'].append(usr)
        return result

class getIolState(BrowserView):
    def __call__(self, *args, **kwargs):
        doc = self.aq_parent
        return api.content.get_state(obj=doc)
