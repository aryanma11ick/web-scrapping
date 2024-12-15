from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("products", views.product_grid, name="products"),
    path("product/<int:product_id>/", views.product_details, name='product_detail'),

]
