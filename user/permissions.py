from . import models, serializers
from user.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

User = get_user_model()
# Create your views here.


class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_librarian is True:
            return True
        else:
            return False


class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_member is True:
            return True
        else:
            return False