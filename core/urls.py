
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'index.html'), name="homepage"),
    path('dashboard/', include("dashboard.urls")),
    path('auth/', include("authentication.urls")),
    path('api/', include("dashboard_API.urls"))
]
