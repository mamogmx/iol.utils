from Products.CMFCore.utils import getToolByName
from plone.dexterity.browser.view import DefaultView
from plone import api
from iol.utils.interfaces import IIolDocument
from iol.utils import config
from zope.component import getUtility


# Get Iol Role on Object
class getIolRoles(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        doc = self.aq_parent
        app = doc.getItem(config.APP_FIELD,config.APP_FIELD_DEFAULT_VALUE)
        utils = getUtility(IIolDocument,app)
        return utils.getIolRoles(doc)













# Get Workflow State
class getState(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        doc = self.aq_parent
        return api.content.get_state(obj=doc)

# List of all available Transition
class getTransitions(object):

    def __init__(self,context,request):
        self.context = context
        self.request = request

    def __call__(self):
        return ""

#
class wfInfo(object):

    def __init__(self,context,request):
        self.context = context
        self.request = request

    def __call__(self):
        return ""

class nextNumber(object):

    def __init__(self,context,request):
        self.context = context
        self.request = request

    def __call__(self,field='numero_pratica'):
        return ""

class createDocx(object):

    def __init__(self,context,request):
        self.context = context
        self.request = request

    def __call__(self):
        return ""