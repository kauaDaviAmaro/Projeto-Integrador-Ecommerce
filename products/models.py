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
        return f"{self.name} - R${self.price:.2f}"

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
    


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    atributesSelected = models.CharField(max_length=100)
    image = models.ImageField(upload_to='orders/', null=True, blank=True)
    description = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk} - Total: R${self.total_price:.2f}"