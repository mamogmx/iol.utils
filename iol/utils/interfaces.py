from zope.interface import Interface, implements
from plone import api
from AccessControl import ClassSecurityInfo

class IIolDocument(Interface):
    """
    marcker interface for iol document
    """
class IolDocument(object):
    security = ClassSecurityInfo()

    implements(IIolDocument)
    security.declarePublic('getIolStatus')
    def getIolStatus(self):
        return api.content.get_state(obj=self)



class IIolLayer(Interface):
    """Marker interface for the Browserlayer
    """


