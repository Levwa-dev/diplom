from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    picture = models.ImageField(verbose_name='Фото', upload_to='product/')
    price = models.IntegerField( verbose_name='Ціна')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категорія', default=None)
    discount = models.BooleanField( verbose_name='Знижка', default=False)
    inStock = models.BooleanField(verbose_name='В наявності', default=True)
    incart = models.BooleanField(default=False)
    summaryPrice = models.IntegerField(default=0)
    quantit = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

class Character_value(models.Model):
    character = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категорія')
    name = models.CharField(max_length=100, verbose_name="Назва характеристики")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характеристику"
        verbose_name_plural = "Характеристики"

class Character_value_v(models.Model):
    character = models.ForeignKey(Character_value, on_delete=models.CASCADE, verbose_name='Назва характеристики',
                                  related_name='characters_value')
    description = models.CharField(max_length=100, verbose_name="Опис характеристики")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = " Значение характеристики"
        verbose_name_plural = "Значение характеристик"

class ProductCharacter(models.Model):
    character = models.ForeignKey(Character_value, on_delete=models.CASCADE, verbose_name="Назва характеристики",
                                  related_name='characters')
    chararacter_v = models.ForeignKey(Character_value_v, on_delete=models.CASCADE, verbose_name='Значення характеристики')
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='characters')

    class Meta:
        verbose_name = " Значення характеристики"
        verbose_name_plural = "Характеристики продукту"

    def __str__(self):
        return self.chararacter_v.description

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/', verbose_name='Фото')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Слайди', related_name='slides')

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайди"

    def __str__(self):
        ms = str(self.id)
        return ms

class Order_s_info(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Им'я")
    last_name = models.CharField(max_length=150, verbose_name='Прізвище')
    patronymic = models.CharField(max_length=150, verbose_name='По батькові')
    telephone = models.CharField(max_length=50, verbose_name='Телефон')
    region = models.CharField(max_length=150, verbose_name='Область')
    city = models.CharField(max_length=150, verbose_name='Місто')
    delivery = models.CharField(max_length=150, verbose_name='Спосіб доставки')
    post = models.CharField(max_length=150, verbose_name='Номер відділення пошти')
    payment = models.CharField(max_length=150, verbose_name='Спосіб оплати')
    total = models.IntegerField(verbose_name="Вартість замовлення", default=0)
    date = models.DateTimeField(verbose_name='Час замовлення', default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name='Замовлення'
        verbose_name_plural = "Замовлення"

class MyUserManager(BaseUserManager):
    def _create_user(self, email,  password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели почту")
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password, first_name, last_name):
        return self._create_user(email, password, first_name, last_name)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    class Meta():
        verbose_name = 'Користувача'
        verbose_name_plural = "Користувачі"

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key = True, unique = True)
    email = models.EmailField(max_length=100, unique=True,verbose_name="email")
    first_name = models.CharField(max_length=100,verbose_name="Имя")
    last_name = models.CharField(max_length=100,verbose_name="Фамилия")
    is_active = models.BooleanField(default=True,verbose_name="Активирован")
    is_staff = models.BooleanField(default=False,verbose_name="Администратор")
    is_superuser = models.BooleanField(default=False, verbose_name="Администратор")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name= 'Дата регистрации')

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['first_name','last_name','usreview','usproduct']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    class Meta():
        verbose_name = 'Користувача'
        verbose_name_plural = "Користувачі"


class Review(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    text = models.TextField(max_length=5000, verbose_name='Коментарий')
    date = models.DateField(default=timezone.now, verbose_name= 'Был написан')
    parent = models.ForeignKey('self',
                               verbose_name='Отзыв на коментарий', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='children')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Отзыв',
                             related_name='usreview')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.product}"

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = "Коментарі"


class Order_product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Назва')
    quantity = models.IntegerField(verbose_name="Кількість", default=0)
    price = models.CharField(max_length=150, verbose_name="Ціна", default=None)
    order_id = models.ForeignKey(Order_s_info, on_delete=models.CASCADE)
    product_id = models.IntegerField(verbose_name="Id товару", default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Користувач',
                             related_name='usproduct')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукти"


