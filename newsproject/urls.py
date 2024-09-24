from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsapp. urls')),  # include URL patterns from news app
]

