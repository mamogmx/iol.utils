from zope.interface import Interface, implements
from zope.component import adapts
from plone import api
from AccessControl import ClassSecurityInfo
from Products.CMFPlomino.interfaces import IPlominoDocument

class IIolDocument(Interface):
    """
    marcker interface for iol document
    """
class IolDocument(object):
    security = ClassSecurityInfo()

    implements(IIolDocument)
    adapts(IPlominoDocument)

    def __init__(self, doc):
        self = doc

    security.declarePublic('getIolStatus')
    def getIolStatus(self):
        return api.content.get_state(obj=self)

class IIolLayer(Interface):
    """Marker interface for the Browserlayer
    """


