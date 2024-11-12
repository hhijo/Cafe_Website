from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('blog/',views.blog,name='my_blog'),
    path('coffees/',views.coffees,name='my_coffees'),
    path('contact/',views.contact,name='my_contact')
]