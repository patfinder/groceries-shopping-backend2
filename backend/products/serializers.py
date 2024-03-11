from rest_framework import serializers

from backend.products.models import CommonProductName, Product


class CommonProductNameSerializer(serializers.HyperlinkedModelSerializer):  # new
    # owner = serializers.ReadOnlyField(source="owner.username")
    # highlight = serializers.HyperlinkedIdentityField(  # new
    #     view_name="product-highlight", format="html"
    # )

    class Meta:
        model = CommonProductName
        fields = '__all__'
        

class ProductSerializer(serializers.HyperlinkedModelSerializer):  # new
    # owner = serializers.ReadOnlyField(source="owner.username")
    # highlight = serializers.HyperlinkedIdentityField(  # new
    #     view_name="product-highlight", format="html"
    # )

    class Meta:
        model = Product
        fields = '__all__'

