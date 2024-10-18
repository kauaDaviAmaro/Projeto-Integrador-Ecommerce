from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from .models import Product, Attribute, AttributeValue, ProductAttributeValue

class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1

    def image_tag(self, obj):
        if obj.product.image:
            return mark_safe(f'<img src="{obj.product.image.url}" width="50" height="50" />')
        return '-'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'is_active', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    
    image_tag.short_description = 'Image'
    inlines = [ProductAttributeValueInline]
    # Adicionar um título traduzido
    verbose_name = _("Produtos")
    verbose_name_plural = _("Products")

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1

class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]
    verbose_name = _("Attribute")
    verbose_name_plural = _("Attributes")

# Registrar os modelos no admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute, AttributeAdmin)