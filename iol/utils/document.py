from zope.interface import implements
from copy import deepcopy

from Products.CMFPlomino.interfaces import IPlominoDocument

class IOLDocument(object):
    implements(IPlominoDocument)

    def __init__(self,context,request):
        self.context = context
        self.request = request

    def getIolRoles(self):
        result = dict(
            iol_owner = [],
            iol_reviewer = [],
            iol_manager = [],
        )
        for usr,roles in self.get_local_roles():
            if 'Owner' in roles:
                result['iol_owner'].append(usr)
            if 'iol-reviewer' in roles:
                result['iol_reviewer'].append(usr)
            if 'iol-manager' in roles:
                result['iol_manager'].append(usr)
        return result