from django.contrib import admin

from product import models


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'in_stock', 'date_added')
    list_filter = ('date_added', )
    inlines = [
        ProductImageInline,
    ]


# admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Feature)
admin.site.register(models.Category)
admin.site.register(models.Review)