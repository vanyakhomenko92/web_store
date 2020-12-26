from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAmin(admin.ModelAdmin):
    list_display =  [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    class Meta:
        model = Product

admin.site.register(Product, ProductAmin)

class ProductImageAmin(admin.ModelAdmin):
    list_display =  [field.name for field in ProductImage._meta.fields]
    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAmin)