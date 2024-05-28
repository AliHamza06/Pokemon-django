from django.urls import path
from . import views
from .views import (
    home,
    leaderBoard,
    whitePaper,
)
urlpatterns = [
    path('', home , name = 'home'),
    path('leader-board/', leaderBoard, name = 'leader-board'),
     path('white-paper/', whitePaper, name = 'white-paper'),
]