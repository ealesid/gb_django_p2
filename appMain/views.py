from rest_framework import viewsets

from appMain.serializers import *


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited
    """
    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductsSerializer


class ProductCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ProductCategories.objects.all().order_by('name')
    serializer_class = ProductCategoriesSerializer


class ProductLightSourcesViewSet(viewsets.ModelViewSet):
    queryset = ProductLightSources.objects.all().order_by('name')
    serializer_class = ProductLightSourcesSerializer


class ProductManufacturersViewSet(viewsets.ModelViewSet):
    queryset = ProductManufacturers.objects.all().order_by('name')
    serializer_class = ProductManufacturersSerializer


class ProductResolutionsViewSet(viewsets.ModelViewSet):
    queryset = ProductResolutions.objects.all().order_by('name')
    serializer_class = ProductResolutionsSerializer


class ProductTypesViewSet(viewsets.ModelViewSet):
    queryset = ProductTypes.objects.all().order_by('name')
    serializer_class = ProductTypesSerializer
