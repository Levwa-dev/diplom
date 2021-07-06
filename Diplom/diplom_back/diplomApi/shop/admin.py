from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import Photo, Product, Categories, Character_value, Character_value_v,ProductCharacter,Order_s_info,Order_product,\
    Review, User

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class CharInline(admin.StackedInline):
    model = ProductCharacter
    extra = 1

class CharValueInline(admin.StackedInline):
    model = Character_value_v
    extra = 1

class OrderInline(admin.StackedInline):
    model = Order_product
    extra = 0

class Character_valueAdmin(admin.ModelAdmin):
    list_display = ('name', 'character')
    list_filter = ('character',)
    search_fields = ('name',)
    inlines = [CharValueInline]

class Order_s_infoAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date','payment')
    list_filter = ('payment',)
    search_fields = ('first_name', 'last_name', 'date')
    inlines = [OrderInline]

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','first_name', 'last_name', 'password', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name','last_name', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, CharInline]
    list_display = ('name','price','category','discount')
    list_filter = ('category','inStock')
    search_fields = ('name','id','price')
    change_form_template = 'admin.html'
    exclude = ['incart', 'summaryPrice', 'quantit']

admin.site.register(Product,ProductAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Categories)
admin.site.register(Order_s_info,Order_s_infoAdmin)
admin.site.register(Character_value,Character_valueAdmin)
admin.site.register(Review)

admin.site.site_header = 'Адміністративна панель магазину "IT-GALAXY"'

