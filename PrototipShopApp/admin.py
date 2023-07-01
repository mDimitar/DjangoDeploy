from django.contrib import admin
from .models import Category, Type, Product, Brand, ShoppingCart

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","description"]

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
admin.site.register(Category, CategoryAdmin)

class TypeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
admin.site.register(Type, TypeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description","category","brand","type"]

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
admin.site.register(Product, ProductAdmin)

class BrandAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
admin.site.register(Brand, BrandAdmin)

class ShoppingCartAdmin(admin.ModelAdmin):

    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return True


admin.site.register(ShoppingCart, ShoppingCartAdmin)
