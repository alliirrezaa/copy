from django.urls import path
from .views import *

app_name='orders'
urlpatterns = [
    path('detail/',order_Detail,name='orders_detail'),
    path('history/',orderHitory.as_view(),name='history'),
]
