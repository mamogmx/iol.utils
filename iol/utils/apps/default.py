# -*- coding: utf-8 -*-
from zope.interface import implements
from iol.utils.interfaces import IIolDocument
from zope import component
from AccessControl import ClassSecurityInfo
from plone import api

from gisweb.iol.permissions import IOL_READ_PERMISSION, IOL_EDIT_PERMISSION, IOL_REMOVE_PERMISSION

from iol.utils.config import USER_CREDITABLE_FIELD,USER_UNIQUE_FIELD,IOL_APPS_FIELD,STATUS_FIELD
from Products.CMFCore.utils import getToolByName



class defaultApp(object):
    implements(IIolDocument)
    security = ClassSecurityInfo()
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        pass
    #Returns dict with all roles->users/groups defined in Iol application
    security.declarePublic('getIolRoles')
    def getIolRoles(self,obj):
        result = dict(
            iol_owner=[],
            iol_viewer=[],
            iol_reviewer = [],
            iol_manager = [],
        )
        for usr,roles in obj.get_local_roles():
            if 'Owner' in roles:
                result['iol_owner'].append(usr)
            if 'iol-viewer' in roles:
                result['iol_viewer'].append(usr)
            if 'iol-reviewer' in roles:
                result['iol_reviewer'].append(usr)
            if 'iol-manager' in roles:
                result['iol_manager'].append(usr)
        return result

    #returns misc infos about workflow
    security.declareProtected('IOL_READ_PERMISSION','getWfInfo')
    def getWfInfo(self):
        result = dict()
        return result

    #Assign selected user to Iol Groups
    def _assignGroups(self,obj,username,grps):
        portal_groups = getToolByName(obj, 'portal_groups')
        for grp in grps:
            portal_groups.addPrincipalToGroup(username, grp)

    #remove selected user from groups
    def _removeGroups(self,obj,username,grps):
        portal_groups = getToolByName(obj, 'portal_groups')
        for grp in grps:
            portal_groups.removePrincipalToGroup(username, grp)

    #Assign ownership to selected user
    def _assignOwner(self,obj,user,add=True):
        if add:
            username = user.get('username','')
            obj.manage_setLocalRoles(username, ["Owner",])
        else:
            obj.changeOwnership(user)
        obj.reindexObjectSecurity()

    #Procedure that search all documents of the selected user, assign him ownership, and move him in iol groups
    security.declarePublic('accreditaUtente')
    def accreditaUtente(self,obj):
        user = obj.getOwner()
        username = user.get('username','')
        apps = obj.getItem(IOL_APPS_FIELD,[])

        #for appName in apps:
            #app = App(appName)
            #for grp in app.getOwnerGroups():
            #    self._assignGroups(obj,username,[grp])
        self._assignGroups(obj,username,apps)

        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog(portal_type='PlominoDatabase')
        unique = obj.getItem(USER_UNIQUE_FIELD,'')
        cont = 0
        for brain in brains:
            db = brain.getObject()
            idx = db.getIndex()
            req = dict(USER_CREDITABLE_FIELD = unique)
            for br in idx.dbsearch(req,only_allowed=False):
                doc = br.getObject()
                self._assignOwner(doc,user)
                cont += 1
        return cont
    security.declarePublic('updateStatus')
    def updateStatus(self,obj):
        obj.setItem(STATUS_FIELD,api.content.get_state(obj=obj) )
        self.reindex_doc(obj)

    security.declarePublic('reindex_doc')
    def reindex_doc(self,obj):
        db = obj.getParentDatabase()
        # update index
        db.getIndex().indexDocument(obj)
        # update portal_catalog
        if db.getIndexInPortal():
            db.portal_catalog.catalog_object(obj, "/".join(db.getPhysicalPath() + (obj.getId(),)))

    security.declarePublic('createPdf')
    def createPdf(selfself,obj,filename,itemname,overwrite):
        filename = '%s.pdf' % filename or obj.REQUEST.get('filename') or obj.getId()

        try:
            res = obj.restrictedTraverse('@@wkpdf').get_pdf_file()
        except Exception as err:

            msg1 = "%s" % (str(err))
            msg2 = "Attenzione! Non è stato possibile allegare il file: %s" % filename
            api.portal.show_message(message=msg1, request=obj.REQUEST,type='error')
            api.portal.show_message(message=msg2, request=obj.REQUEST,type='warning')
        else:
            (f,c) = obj.setfile(res,filename=filename,overwrite=overwrite,contenttype='application/pdf')
            if f and c:
                old_item = obj.getItem(itemname, {}) or {}
                old_item[filename] = c
                obj.setItem(itemname, old_item)

#############################################################################
app = defaultApp()
gsm = component.getGlobalSiteManager()
gsm.registerUtility(app, IIolDocument, 'default')
