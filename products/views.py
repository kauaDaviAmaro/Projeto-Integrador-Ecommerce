from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductAttributeValue, Order

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

def product_design(request, product_id):
    if request.method != 'POST':
        raise Http404("Page not found")

    product = get_object_or_404(Product, pk=product_id)

    attributesSelected = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}

    template = "productDesign.html"
    return render(request, template, {'product': product, 'attributesSelected': attributesSelected})

def order_product(request, product_id):
    if request.method != 'POST':
        raise Http404("Page not found")
    
    product = get_object_or_404(Product, pk=product_id)

    type = request.POST.get('type')
    image = None
    if type == 'image':
        image = request.FILES.get('design')
    

    order = Order(
        product=product,
        atributesSelected=request.POST.get('attributes'),
        image=image,
        description=request.POST.get('description'),
        name=request.POST.get('name'),
        email=request.POST.get('email'),
        phone=request.POST.get('phone'),
        street=request.POST.get('street'),
        number=request.POST.get('number'),
        district=request.POST.get('district'),
        city=request.POST.get('city'),
        state=request.POST.get('state'),
        zip_code=request.POST.get('zip_code')
    )
    order.save()
    template = "order_success.html"
    return render(request, template)

def order_success(request):
    template = "order_success.html"
    return render(request, template)