from django.urls import path , include
from .views import current_datetime,GetVoters

urlpatterns = [
    path('date', current_datetime),
    path('voters', GetVoters.as_view(),name='voters')
]