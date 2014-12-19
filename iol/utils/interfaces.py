from zope.interface import Interface

class IIolDocument(Interface):
    def __init__(self, context, request):
        self.context = context
        self.request = request

class IIolLayer(Interface):
    """Marker interface for the Browserlayer
    """