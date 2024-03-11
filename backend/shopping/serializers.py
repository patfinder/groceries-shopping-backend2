from rest_framework import serializers

from backend.shopping.models import WishListItem


class WishListItemSerializer(serializers.ModelSerializer):  # new
    class Meta:
        model = WishListItem
        fields = '__all__'
