from django.urls import path
from .views import * 
urlpatterns = [
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('user/',UserView.as_view(),name='user'),
    path('logout/',Logout.as_view(),name='logout'),

]