from zope.interface import Interface, implements
from zope.component import adapts
from plone import api
from AccessControl import ClassSecurityInfo
from Products.CMFPlomino.interfaces import IPlominoDocument

class IIolDocument(Interface):
    """
    marker interface for iol document
    """




class IIolLayer(Interface):
    """Marker interface for the Browserlayer
    """


