from pprint import pprint
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class IsPleasantHabit(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request:
            pprint(request.data)
            return True
        else:
            return False
