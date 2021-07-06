
from django.urls import path

from .api_views import CharacterSerializerView, CategoriesSerializerView, \
    ProductsSerializerView, ProductSerializerView, OrdersSrializerView,\
    OrdersProductSrializerView, ProductsCategoriesSerializerView, RegistrUserView,ReviewCreateView, PayForOrderView,\
    PayResponse



urlpatterns = [
        path('characters/<int:pk>/', CharacterSerializerView.as_view()),
        path('categories/', CategoriesSerializerView.as_view()),
        path('products/', ProductsSerializerView.as_view()),
        path('products/<int:pk>/', ProductSerializerView.as_view()),
        path('order_s_info/',OrdersSrializerView.as_view()),
        path('product_categories/<int:id>/', ProductsCategoriesSerializerView.as_view()),
        path('order_product/',OrdersProductSrializerView.as_view()),
        path('review/',ReviewCreateView.as_view()),
        path('registr/', RegistrUserView.as_view()),
        path('payUrl/', PayForOrderView.as_view()),
        path('payResponse/', PayResponse.as_view()),

]