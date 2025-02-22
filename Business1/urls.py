
from django.contrib import admin
from django.urls import path
from faidaapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('inventory/', views.inventory),
    path('services/', views.services),
]
