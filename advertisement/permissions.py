from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    # работа с одним объектом (для update, delete, details)
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user