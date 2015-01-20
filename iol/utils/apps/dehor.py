from default import defaultApp
from zope import component

class dehor(defaultApp):
    def __init__(self):
        pass

app = dehor()
gsm = component.getGlobalSiteManager()
gsm.registerUtility(app, IIolDocument, 'dehor')
