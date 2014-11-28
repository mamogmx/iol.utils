# -*- extra stuff goes here -*-
from Products.CMFPlomino.PlominoForm import PlominoForm
from Products.CMFPlomino.PlominoDocument import PlominoDocument
from plone import api
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass

from Products.CMFPlomino.config import EDIT_PERMISSION
from Products.CMFPlomino.config import READ_PERMISSION

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

InitializeClass(PlominoDocument)        
PlominoDocument.security = ClassSecurityInfo()     
    
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
    
def verificaRuolo(self,ruolo=''):
    roles = self.portal_membership.getAuthenticatedMember().getRolesInContext(self)
    return ruolo in roles or 'Manager' in roles
    
PlominoDocument.security.declareProtected(READ_PERMISSION, 'getIolRoles')
PlominoDocument.getIolRoles = getIolRoles   

PlominoDocument.security.declareProtected(READ_PERMISSION, 'verificaRuolo')
PlominoDocument.verificaRuolo = verificaRuolo   
   