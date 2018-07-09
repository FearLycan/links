from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.homepage.index, name='homepage'),
    path('link', views.link.index, name='link'),
]
