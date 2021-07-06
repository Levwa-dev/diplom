from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated

from cloudipsp import Api, Checkout

from rest_framework.response import Response

from rest_framework.generics import ListAPIView, CreateAPIView


from rest_framework.views import APIView

from ..models import Character_value, Product, Categories, User

from .serializers import CharacterSerializer, ProductSerializer,CategoriesSerializer, Order_s_infoSerializer,\
    Order_productSerializer, ProductDetailSerializer, UserRegistrSerializer, ReviewCreateSerializer

# Вывод характеристик категории
class CharacterSerializerView(APIView):
    def get(self, request, pk):
        character = Character_value.objects.filter(character=pk)
        serializer = CharacterSerializer(character,
                                         many=True, context={"request":request})
        return Response(serializer.data)
# Вывод по категориям
class ProductsCategoriesSerializerView(APIView):
     def get(self, request, id):
         products = Product.objects.filter(category=id)
         serializer = ProductSerializer(products,
                                        many = True, context={"request":request})
         return Response(serializer.data)

# Категории
class CategoriesSerializerView(ListAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


# Продукты
class ProductsSerializerView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# Продукт
class ProductSerializerView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializer(product, context={"request":request})
        return Response(serializer.data)


# POST информация о заказаных продуктах
class OrdersProductSrializerView(APIView):
    def post(self, cart):
        order_product = Order_productSerializer(data=cart)
        if order_product.is_valid():
            order_product.save()
        return Response(status=201)


# POST информация о пользователе
class OrdersSrializerView(APIView):
    def post(self, request):
        order_s_info = Order_s_infoSerializer(data=request.data)
        s = request.data.copy()
        carts = s.pop('cart')
        if order_s_info.is_valid():
            instance = order_s_info.save()
            instance_id = instance.id
            for cart in carts:
                cart['order_id'] = instance_id
                OrdersProductSrializerView.post(self, cart)
        return Response(status=201)


class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewCreateSerializer

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
            return Response(status=201)
        else:
            data = review.errors
            return Response(data)

class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'status': 'true'}
            return Response(data, status=200)
        else:
            data = {'status':'Email уже занят'}
            return Response(data)

class PayForOrderView(APIView):
    def post(self, request):
        api = Api(merchant_id=1397120,
                  secret_key='test')
        checkout = Checkout(api=api)
        order = request.data['amount']
        data = {
            "currency": "UAH",
            "amount": order * 100,
            "order_desc": 'Покупка товарів на сайті IT-GALAXY',
            "response_url":"http://127.0.0.1:8000/api/payResponse/",
        }
        url = checkout.url(data).get('checkout_url')
        data = {'payUrl': url}
        return Response(data)

class PayResponse(APIView):
    status = 'notallowed'

    def post(self, request):
        data = request.data.copy()
        statusFondy = data.pop('order_status')
        if statusFondy[0] == 'approved':
            PayResponse.status = statusFondy[0]
            return redirect('http://localhost:8080/confirm')
        else:
            return Response(status=400)

    def get(self, request):
        getStatus = self.status
        data = {
            'response': getStatus
        }
        PayResponse.status='notallowed'
        return Response(data)

