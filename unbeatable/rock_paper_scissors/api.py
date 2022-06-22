from django.urls import path
from .views import RockPaperScissorsComputerPlay

app_name = 'rock_paper_scissors'

urlpatterns = [
    path('<str:slug>', RockPaperScissorsComputerPlay.as_view(), name='computer-play'),
]
