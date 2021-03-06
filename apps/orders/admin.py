from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'note', 'status', 'paid', 'created', 'updated', 'pk']
    list_editable = ['status', 'paid']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ['order', 'status', 'pk']
