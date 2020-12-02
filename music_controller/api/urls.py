
from django.urls import path
from .views import RoomView,CreateRoomView,GetRoom

urlpatterns = [

    path("create-room",CreateRoomView.as_view()),
    path("room",RoomView.as_view()),
    path("",RoomView.as_view()),
    path("get-room",GetRoom.as_view()),

]