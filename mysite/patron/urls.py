from django.urls import path, include
#from django.conf import settings #I think I have to remove this
#from django.conf.urls.static import static

from . import views

app_name = 'patron'

urlpatterns = [
    path('', views.home, name="home"),

    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),

]