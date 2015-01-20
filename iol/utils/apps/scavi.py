from zope.interface import implements
from iol.utils.interfaces import IIolDocument
from zope import component

class scaviApp(object):
    implements(IIolDocument)

    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        pass

    def getIolRoles(self,obj):
        result = dict(
            iol_owner=[],
            iol_viewer=[],
            iol_reviewer = [],
            iol_manager = [],
        )

        return result
    def getWfInfo(self):
        result = dict()
        return result

app = scaviApp()
gsm = component.getGlobalSiteManager()
gsm.registerUtility(app, IIolDocument, 'scavi')