
from django.contrib import admin
from django.urls import path, include
from Login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view()),
    path('Miapp/', include('MiApp.urls')),
    path('Home/', include('Homepage.urls')),

]
