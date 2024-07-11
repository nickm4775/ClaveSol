from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    # Auth
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),

    # Admin
    path('admin/', admin.site.urls),

    # Apps
    path("ClaveDeSol/Estudiante/", include("apps.Estudiante.urls")),
    path("ClaveDeSol/Nivel/", include("apps.Nivel.urls")),
    path("ClaveDeSol/Requisito/", include("apps.Requisito.urls")),
    path("ClaveDeSol/Coordinador/", include("apps.Coordinador.urls")),
    path("ClaveDeSol/User/", include("apps.User.urls")),


]
