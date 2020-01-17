from django.contrib import admin
from django.urls import path, include
from contra_partida import urls as contra_partida_urls
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestao/', include(contra_partida_urls)),
    path('', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),

]
