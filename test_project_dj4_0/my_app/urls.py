from django.urls import path

from .views import Client_ListView

app_name = "my_app"

urlpatterns = [
    path('client_list/', Client_ListView.as_view(), name="client_list"),
]
