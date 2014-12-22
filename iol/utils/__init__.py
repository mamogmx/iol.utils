from zope.i18nmessageid import MessageFactory
from zope.component import getGlobalSiteManager
from iol.utils.interfaces import IIolDocument, IolDocument
from Products.CMFPlomino.PlominoDocument import PlominoDocument
from Products.CMFPlomino.interfaces import IPlominoDocument
# Set up the i18n message factory for our package
MessageFactory = MessageFactory('iol.utils')


