from interfaces import IIolDocument
from Products.CMFPlomino.interfaces import IPlominoDocument


def initIolDocument(doc,event):
    import pdb
    pdb.set_trace()
    adapter = IIolDocument(doc,IPlominoDocument,'iol')
    doc.setItem('iol',adapter)

