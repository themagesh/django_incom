from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('1chart.in',include('chart_app.urls')),
    # path('admin/', admin.site.urls),
]
