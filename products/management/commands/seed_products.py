from django.core.management.base import BaseCommand
from products.models import Product, Attribute, AttributeValue, ProductAttributeValue
from faker import Faker
import requests
from django.core.files import File
from io import BytesIO
import os
import uuid
import random


class Command(BaseCommand):
    help = 'Populates the database with products and images from the internet'

    def delete_images(self):
        media_path = 'media/products'
        if os.path.exists(media_path):
            for filename in os.listdir(media_path):
                if filename.endswith(".jpg"):
                    file_path = os.path.join(media_path, filename)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error deleting file {file_path}: {e}'))

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Limpar dados existentes
        Product.objects.all().delete()
        Attribute.objects.all().delete()
        ProductAttributeValue.objects.all().delete()
        self.delete_images()

        # Criar atributos e valores
        attributes = [
            Attribute.objects.create(name='Tamanho'),
            Attribute.objects.create(name='Cor'),
            Attribute.objects.create(name='Material'),
            Attribute.objects.create(name='Gênero'),
            Attribute.objects.create(name='Estilo'),
        ]

        attribute_values = [
            AttributeValue.objects.create(attribute=attributes[0], value='P'),
            AttributeValue.objects.create(attribute=attributes[0], value='M'),
            AttributeValue.objects.create(attribute=attributes[0], value='G'),
            AttributeValue.objects.create(attribute=attributes[1], value='Vermelho'),
            AttributeValue.objects.create(attribute=attributes[1], value='Verde'),
            AttributeValue.objects.create(attribute=attributes[1], value='Azul'),
            AttributeValue.objects.create(attribute=attributes[2], value='Couro'),
            AttributeValue.objects.create(attribute=attributes[2], value='Tecido'),
            AttributeValue.objects.create(attribute=attributes[2], value='Plástico'),
            AttributeValue.objects.create(attribute=attributes[3], value='Feminino'),
            AttributeValue.objects.create(attribute=attributes[3], value='Masculino'),
            AttributeValue.objects.create(attribute=attributes[3], value='Unissex'),
            AttributeValue.objects.create(attribute=attributes[4], value='Clássico'),
            AttributeValue.objects.create(attribute=attributes[4], value='Modern'),
            AttributeValue.objects.create(attribute=attributes[4], value='Retro'),
        ]

        # Criar produtos
        for _ in range(25):
            self.stdout.write(self.style.WARNING('Downloading image...'))
            image_url = f'https://placehold.co/600x400/jpg?text={faker.word()}'

            response = requests.get(image_url)
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR('Failed to download image.'))
                continue

            img = BytesIO(response.content)
            self.stdout.write(self.style.SUCCESS('Image downloaded!'))

            product = Product.objects.create(
                name=faker.word(),
                price=faker.random_int(min=1, max=10000), 
                description=faker.sentence(),
                quantity=faker.random_int(min=0, max=100),
                is_active=True,
            )

            # Salvar a imagem com um nome único
            unique_filename = f"{uuid.uuid4()}.jpg"
            product.image.save(unique_filename, File(img), save=True)

            # Associar múltiplos valores de atributos ao produto
            for attribute in attributes:
                # Selecionar múltiplos valores aleatórios para o atributo
                attribute_values = AttributeValue.objects.filter(attribute=attribute)
                selected_values = random.sample(list(attribute_values), k=min(3, len(attribute_values)))  # Seleciona até 2 valores

                for attribute_value in selected_values:
                    ProductAttributeValue.objects.create(
                        product=product,
                        attribute_value=attribute_value
                    )

        self.stdout.write(self.style.SUCCESS('Product seed with images downloaded from the internet completed!'))