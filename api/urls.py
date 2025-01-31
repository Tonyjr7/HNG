from django.urls import path
from api.views import ListME

urlpatterns = [
     path('', ListME.as_view(), name='list_me'),
]