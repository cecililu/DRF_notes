from rest_framework import permissions


class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        print(request.method)
        if request.method in ['GET']:
            return True

        print('has_permissions')
        if request.user.is_authenticated:
            return True
        

    def has_object_permission(self, request, view, obj):
        print('has_permissions onject run')
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        # if obj.author== request.user:
        #     return True
        
        if request.user.is_staff and request.user.muni==obj.muni:
            return True
        return False