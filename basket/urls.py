from django.urls import  path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='summary'),
    path('add/<int:product_id>/', views.add_to_basket, name='add-to-basket'),
    path('remove/<int:product_id>/', views.remove_from_basket, name='remove-from-basket'),
    path('update/details/', views.update_basket_details, name='update-details'),
    path('update/number/', views.update_basket_number, name='update-number'),
    path('update/footer/', views.update_basket_footer, name='update-footer'),

]
