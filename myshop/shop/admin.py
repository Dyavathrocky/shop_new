from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """this is for category model """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """this is for Product model """
    list_display = ['name','slug','image','price','avilable','created','updated']
    list_filter = ['name','avilable','created','updated']
    list_editable = ['price','avilable']
    prepopulated_fields = {'slug':('name',)}

