from zope.interface import Interface

class IIolDocument(Interface):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getIolRoles(self):
        result = dict(
            iol_owner=[],
            iol_reviewer = [],
            iol_manager = [],
        )
        for usr,roles in self.get_local_roles():
            if 'Owner' in roles:
                result['iol_owner'].append(usr)
            if 'iol-reviewer' in roles:
                result['iol_reviewer'].append(usr)
            if 'iol-manager' in roles:
                result['iol_manager'].append(usr)
        return result