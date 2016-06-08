from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^store/', views.store, name='index'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
]
