from django.urls import path
from . import views
urlpatterns=[
    path('main',views.mainfn,name='main'),
    path('master',views.master,name='master'),
    path('add',views.add,name='add'),
    path('search',views.search,name='search')

]