from django.urls import path

from .views import IndexView


urlpatterns = [
    path('home/', IndexView.as_view(), {'name': 'Home'}, name='home'),
    path('about/', IndexView.as_view(), {'name': 'About company'},
         name='company'),
    path('auto_parts/', IndexView.as_view(), {'name': 'Auto Parts'},
         name='auto_parts'),
    path('auto_parts/transmission', IndexView.as_view(),
         {'name': 'Auto Transmission'}, name='auto_parts_transmission'),
    path('prices/', IndexView.as_view(), {'name': 'Prices'}, name='prices'),
]
