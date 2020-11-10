from .serializers import RoomSerializer
from rest_framework import serializers
from .models import Room
from django.shortcuts import render
from rest_framework import generics


class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

class RoomCreate(generics.CreateAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer