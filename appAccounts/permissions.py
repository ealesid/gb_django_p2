from rest_framework.permissions import BasePermission


class IsStaffOrTargetUser(BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        print('has-permission ->\t', request, view.action)
        return view.action == 'exist' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        print('has_object_permission ->\t', request.user, obj)
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user
