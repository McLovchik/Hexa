from django.urls import path
from django.views.decorators.cache import cache_page

from .views import IndexView, ProductsListView, basket_add, basket_remove

app_name = 'app_store'

urlpatterns = [
    path('', cache_page(20)(IndexView.as_view()), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('products/page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/delete/<int:basket_id>/', basket_remove, name='basket_remove'),
]
