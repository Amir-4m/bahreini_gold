from django.urls.conf import path

from .views import ProductList

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),

]
