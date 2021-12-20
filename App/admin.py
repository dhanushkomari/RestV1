from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_id', 'category_name']
    list_per_page = 50
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)