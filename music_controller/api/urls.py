
from django.urls import path
from .views import RoomView,RoomCreate

urlpatterns = [

    path("createroom",RoomCreate.as_view()),
    path("",RoomView.as_view()),

]