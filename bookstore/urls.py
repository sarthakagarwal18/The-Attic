from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('store.urls'), name='store'),
    url(r'^admin/', admin.site.urls),
    #includes urls that the registartion model comes with
    url(r'^accounts/',include('registration.backends.default.urls')),
    #includes urls for social app
    #by using namespace, we can avoid using regex expressions
    url('',include('social.apps.django_app.urls', namespace = 'social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
