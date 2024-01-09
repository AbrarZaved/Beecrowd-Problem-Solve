from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
<<<<<<< HEAD
    path('users/',include('users.urls')),
=======
>>>>>>> 049d486318770b0a0febe5699e65ef117c930f2c
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)  
