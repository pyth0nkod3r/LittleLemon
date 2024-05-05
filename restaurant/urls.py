from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import MenuItem, SingleMenu, index

urlpatterns = [
    path("", index, name="index"),
    path("menu/", MenuItem.as_view(), name="menu"),
    path("menu/<int:pk>/", SingleMenu.as_view(), name="single_menu"),
    path("api-token-auth/", obtain_auth_token),
]
