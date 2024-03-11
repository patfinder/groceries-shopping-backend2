from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import viewsets  # new
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import WishListItem
# from .permissions import IsOwnerOrReadOnly  
from .serializers import WishListItemSerializer


class WishListSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WishListItem.objects.all()
    serializer_class = WishListItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        now = datetime.now()
        serializer.save(created_time=now, updated_time=now)


class ShoppingListSet(viewsets.ModelViewSet):
    queryset = WishListItem.objects.all()
    serializer_class = WishListItemSerializer
    # permission_classes = [permissions.IsAuthenticated]
