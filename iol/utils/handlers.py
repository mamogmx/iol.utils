from Products.CMFPlomino.PlominoDocument import PlominoDocument
from plone import api

class IolDoc(PlominoDocument):
    def getIolStatus(self):
        return api.content.get_state(obj=self)


def initIolDocument(doc,event):
    doc = IolDoc(doc)
    return doc

