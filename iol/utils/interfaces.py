from zope.interface import Interface, implements, Attribute
from zope.component import adapts
from plone import api
from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from Products.CMFPlomino.interfaces import IPlominoDocument, IPlominoForm
from zope.component import getGlobalSiteManager
from iol.utils import config
from zope.component import getUtility

class IIolDocument(Interface):
    """
    marker interface for iol document
    """
    iol_app = Attribute("Application Name")


class IIolLayer(Interface):
    """Marker interface for the Browserlayer
    """

class IolDocument(object):
    implements(IIolDocument)
    adapts(IPlominoForm,IPlominoDocument)
    tipo_app = u""
    security = ClassSecurityInfo()
    security.declareObjectPublic()
    def __init__(self,obj):
        self.document = obj

    security.declarePublic('getIolRoles')
    def getIolRoles(self):
        app = self.document.getItem(config.APP_FIELD,config.APP_FIELD_DEFAULT_VALUE)
        utils = getUtility(IIolDocument,app)
        return utils.getIolRoles(self.document)


InitializeClass(IolDocument)