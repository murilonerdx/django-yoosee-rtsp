from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

# suas outras configurações de URL...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livestream.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

