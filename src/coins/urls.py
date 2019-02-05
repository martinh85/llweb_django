from django.urls import path

from .views import home

from static.inputs import menu_coins

urlpatterns = [
	path('', home),
    #path('indicators/', ('coins.urls', namespace='coins')),
    #for item in menu_coins:
    #	path('item', )
    ]
