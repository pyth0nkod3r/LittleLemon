from django.shortcuts import render
from rest_framework.generics import (
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)

from .models import Menu
from .serializers import MenuSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItem(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItem(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
