from rest_framework import generics
from account.serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountCreateSerializer



class ProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated,IsOwner]

    def get_object(self):
        return self.request.user

