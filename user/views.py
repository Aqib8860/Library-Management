from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from .permissions import IsLibrarian, IsMember
from rest_framework.permissions import AllowAny
#from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, generics


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsLibrarian]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"msg": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(is_member=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)