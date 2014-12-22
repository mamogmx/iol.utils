from zope.i18nmessageid import MessageFactory
from AccessControl import allow_module
MessageFactory = MessageFactory('iol.utils')

allow_module('iol.utils.IolDocument')