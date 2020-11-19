from rest_framework import serializers
from rest_framework import fields
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        # fields=('id','code','host','guest_can_pause',
        #         'votes_to_skip','created_at')

        fields=('__all__')


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('guest_can_pause','votes_to_skip')