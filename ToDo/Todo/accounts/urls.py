from django.urls import path
from accounts.views import registration_view

app_name = "accounts"

urlpatterns = [
    path('register/', registration_view),
]
