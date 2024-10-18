from django.db import models
import os
import uuid

def product_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    
    filename = f'{uuid.uuid4()}.{ext}'
    
    return os.path.join('products/', filename)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()
    image = models.ImageField(upload_to=product_image_file_path, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

    class Meta:
        ordering = ['name']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Attribute(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"

class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attributes')
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.attribute_value.attribute.name}: {self.attribute_value.value}"