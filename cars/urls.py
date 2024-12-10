

from django.urls import path
from django.contrib import admin

from . import views
from .views import search

urlpatterns=[
    path("",views.home,name="home"),
    path ("",views.search,name="search"),

    path('admin/', admin.site.urls),

path('search/', views.search, name='search')



]

    # Add other paths here