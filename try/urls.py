from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('blog/',views.handleblogs, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('service/',views.service, name='service'),
    path('login/',views.handlelogin, name='handlelogin'),
    path('logout/',views.handlelogout, name='handlelogout'),
    path('signup/',views.handlesignup, name='handlesignup'),
    path('search',views.search, name='search'),
    
]