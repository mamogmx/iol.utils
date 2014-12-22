from interfaces import IIolDocument
from Products.CMFPlomino.interfaces import IPlominoDocument


def initIolDocument(doc,event):

    adapter = IIolDocument(doc,IPlominoDocument)
    doc.iol = adapter
