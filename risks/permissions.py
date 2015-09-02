from rest_framework import permissions

class IsUserRisk(permissions.BasePermission):
    def has_object_permission(self, request, view, risk):
        if request.user:
            return risk.user == request.user
        return False