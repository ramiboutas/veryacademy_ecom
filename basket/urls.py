from django.urls import  path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket-summary'),
    path('add/<int:product_id>/', views.add_to_basket, name='add-to-basket'),
    path('remove/<int:item_id>/', views.remove_from_basket, name='remove-from-basket'),

]
