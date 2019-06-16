from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage.as_view(),name='home'),
    path('movies_catagries/',views.Movies_cat.as_view(),name='catagory'),
    path('movies_list/',views.Movies_list.as_view(),name='list'),
]