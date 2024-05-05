from django.urls import path

from .views import Menu, SingleMenu, index

urlpatterns = [
    path("", index, name="index"),
    path("menu/", Menu.as_view(), name="menu"),
    path("menu/<int:pk>/", SingleMenu.as_view(), name="single_menu"),
]
