from zope.interface import Interface,implements
from plone import api

class IIolDocument(Interface):
    @property
    def getIolStatus(self):
        return api.content.get_state(obj=self)



class IIolLayer(Interface):
    """Marker interface for the Browserlayer
    """


