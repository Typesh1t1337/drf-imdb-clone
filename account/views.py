from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from account.serializers import *


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountCreateSerializer





