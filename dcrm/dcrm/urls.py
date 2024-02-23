from django.contrib import admin
from django.urls import path, include
# პათერნებში გავუშვით website ფოლდერის urls ფაილი
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls'))
]
