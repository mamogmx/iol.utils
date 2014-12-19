from zope.component import getUtility

from plone.registry.interfaces import IRegistry
from iol.utils.interfaces import IIolDocument

def iol_document(context=None):  # pylint: disable=W0613
    return getUtility(IRegistry).forInterface(IIolDocument)

