from django.urls import path
from home.views import *
from home.views.loginView import *

urlpatterns = [
    # CustomUser URLs
    path('create_user/', CustomUserView.as_view(), name='create_user'),

    # Role URLs
    path('login/', LoginView.as_view(), name='login'),
    
    
    path('home/', HomeView.as_view(), name='home'),
    path('about/', HomeView.as_view(), name='home'),

]
