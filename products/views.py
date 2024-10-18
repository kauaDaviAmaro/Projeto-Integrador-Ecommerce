from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductAttributeValue

def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'productList.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    attribute_values = ProductAttributeValue.objects.filter(product=product)

    attributes = {}
    for attribute_value in attribute_values:
        attribute_name = attribute_value.attribute_value.attribute.name
        attribute_value_text = attribute_value.attribute_value.value
        if attribute_name not in attributes:
            attributes[attribute_name] = []
        attributes[attribute_name].append(attribute_value_text)

    return render(request, 'productDetail.html', {
        'product': product,
        'attributes': attributes,
    })