from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls', namespace='author')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('', include('book.urls', namespace='book')),

    path('accounts/', include('registration.backends.default.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



