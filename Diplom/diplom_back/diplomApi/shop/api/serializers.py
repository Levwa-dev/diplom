from rest_framework import serializers

from ..models import Character_value_v, Character_value, Product, Photo, Categories, Order_s_info,\
    Order_product, User, Review, ProductCharacter

class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context = self.context)
        return serializer.data

class CharacterValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character_value_v
        fields=('id','description')

class CharacterSerializer(serializers.ModelSerializer):
    characters_value = CharacterValueSerializer(many=True)
    class Meta:
        model = Character_value
        fields="__all__"

class ProductCharacterSerializer(serializers.ModelSerializer):
    character = serializers.CharField(source='character.name')
    chararacter_v = serializers.CharField(source='chararacter_v.description')
    class Meta:
        model = ProductCharacter
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
    photo_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields="__all__"

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields="__all__"

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields=('id','image')


class Order_s_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_s_info
        fields="__all__"

class Order_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_product
        fields="__all__"


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    photo_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    reviews = ReviewSerializer(many=True)
    slides = PhotoSerializer(many=True)
    characters = ProductCharacterSerializer(many=True)

    class Meta:
        model = Product
        fields="__all__"

class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()
    usreview = ReviewSerializer(many=True)
    usproduct = Order_productSerializer(many=True)

    class Meta():
        model = User
        fields= [ 'email', 'password', 'password2', 'first_name', 'last_name', 'usreview','usproduct']

    def save(self, *args, **kwargs):
        user = User(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise  serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user




