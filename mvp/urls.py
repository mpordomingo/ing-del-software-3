"""mvp URL Configuration
"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('testAppIS3.urls')),
]

#path('admin/', admin.site.urls),