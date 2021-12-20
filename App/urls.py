from django.urls import path
from . import views

app_name = 'App'

urlpatterns = [
    path('', views.Home, name = 'home'),
    path('item/<str:prod_id>', views.CatProductView, name = 'cat-prod'),
    path('categories', views.CategoriesView, name = 'cats'),
    path('post-product', views.CreateProduct, name = 'api-post-product'),



    path('add-cat', views.createCat, name = 'add-cat'),
]
