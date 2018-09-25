from rest_framework import serializers

from .models import *


class ProductCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = '__all__'


class ProductLightSourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLightSources
        fields = '__all__'


class ProductManufacturersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManufacturers
        fields = '__all__'


class ProductResolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductResolutions
        fields = '__all__'


class ProductTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypes
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    light_source = serializers.SlugRelatedField(slug_field='name', read_only=True)
    manufacturer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    resolution = serializers.SlugRelatedField(slug_field='name', read_only=True)
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
