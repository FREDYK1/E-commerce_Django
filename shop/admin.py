from django.contrib import admin
from .models import Category, Product, Order, OrderItem


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', "created_at"]
    prepopulated_fields = {'slug': ('name',)}

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category', 'created_at', 'updated_at']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['customer_name', 'customer_email']

class AdminOrderItem(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    list_filter = ['order', 'product']
    search_fields = ['order', 'product']

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderItem, AdminOrderItem)