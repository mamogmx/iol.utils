from Products.CMFCore.utils import getToolByName
from plone.dexterity.browser.view import DefaultView
from plone import api
from iol.utils.interfaces import IIolDocument
from iol.utils import config
from zope.component import getUtility
from iol.utils.interfaces import IolDocument
from five import grok
from Products.CMFPlomino.interfaces import IPlominoDocument


# Get Iol Role on Object
class getIolRoles(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        doc = self.aq_parent
        iDoc = IolDocument(doc)
        return iDoc.getIolRoles(doc)

# Retrieve Objects's WorkFlow Info
class getWfInfo(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        doc = self.aq_parent
        iDoc = IolDocument(doc)
        return iDoc.getWfInfo()



class protocollaInvia(grok.View):

    grok.context(IPlominoDocument)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, *args, **kwargs):
        doc = self.aq_parent
        wf = getToolByName(context, 'portal_workflow') #state_change.workflow
        tr_ids = [i['id'] for i in wf.getTransitionsFor(obj=doc, container=None, REQUEST=None)]

        next_tr = 'protocolla'
        if next_tr in tr_ids:
            wf.doActionFor(context, next_tr)

        IolDocument(context).updateStatus()
        urlAction='%s/content_status_modify?workflow_action=invia_domanda' %(doc.absolute_url())
        doc.REQUEST.RESPONSE.redirect(urlAction)








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