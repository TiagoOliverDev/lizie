from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),  
]
