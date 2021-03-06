from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path("register/",views.register,name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="employee/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="employee/logout.html"),name="logout"),
    path("profile/",views.profile,name="profile"),
    ] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)