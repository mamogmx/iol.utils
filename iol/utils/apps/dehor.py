from default import defaultApp

class dehor(defaultApp):
    def __init__(self):
        pass

app = dehor()
gsm = component.getGlobalSiteManager()
gsm.registerUtility(app, IIolDocument, 'dehor')
