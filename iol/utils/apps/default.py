from zope.interface import implements
from iol.utils.interfaces import IIolDocument
class defaultApp(object):
    implements(IIolDocument)

    def getIolRoles(self):
        result = dict(
            iol_owner=[],
            iol_viewer=[],
            iol_reviewer = [],
            iol_manager = [],
        )
        for usr,roles in self.get_local_roles():
            if 'Owner' in roles:
                result['iol_owner'].append(usr)
            if 'iol-viewer' in roles:
                result['iol_viewer'].append(usr)
            if 'iol-reviewer' in roles:
                result['iol_reviewer'].append(usr)
            if 'iol-manager' in roles:
                result['iol_manager'].append(usr)
        return result

