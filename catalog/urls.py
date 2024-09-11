from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home
from catalog.views import contacts

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
