from zope.i18nmessageid import MessageFactory
from AccessControl import allow_module

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('iol.utils')
allow_module('.interfaces.IolDocument')