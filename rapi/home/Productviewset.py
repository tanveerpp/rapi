from home.Productserializer import ProductSerializer
from home.models import Product
from rest_framework import viewsets
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer