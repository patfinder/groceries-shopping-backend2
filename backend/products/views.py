# from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from backend.products.models import CommonProductName, Product
from backend.products.serializers import CommonProductNameSerializer, ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CommonProductNameViewSet(viewsets.ModelViewSet):
    queryset = CommonProductName.objects.all()
    serializer_class = CommonProductNameSerializer
    # TODO: Get by category


