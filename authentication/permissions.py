from rest_framework import permissions

# Check if the user from the request is the same as the user for the object
class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False