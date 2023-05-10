from django.contrib import admin
from .models import Category, Product


# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_quantity(queryset):
    queryset.update(quantity=0)

nullfy_quantity.short_description = 'Обнулить товары'  # описание для более понятного представления в админ панеле задаётся, как будто это объект

# создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'price', 'description', 'category')  # оставляем только имя и цену товара
    list_filter = ('price', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список

# Register your models here.


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)