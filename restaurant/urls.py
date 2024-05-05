from django.urls import path

from .views import MenuItem, SingleMenuItem, index

urlpatterns = [
    path("", index, name="index"),
    path("menu/", MenuItem.as_view(), name="menu"),
    path("menu/<int:pk>/", SingleMenuItem.as_view(), name="single_menu"),
]
