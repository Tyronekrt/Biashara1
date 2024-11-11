from django.contrib import admin
from django.urls path, include



urlpatterns = [
    path('admin/', admin.site.urls)
    path('', include('faidaapp.url')),

]
