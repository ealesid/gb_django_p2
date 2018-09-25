from django.db import models


class ProductCategories(models.Model):
    name = models.CharField(verbose_name='категория', max_length=24, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class ProductLightSources(models.Model):
    name = models.CharField(verbose_name='источник света', max_length=24, unique=True)
    description = models.TextField(verbose_name='описание типа источника света', blank=True)

    class Meta:
        verbose_name = 'источник света'
        verbose_name_plural = 'источники света'

    def __str__(self):
        return self.name


class ProductManufacturers(models.Model):
    name = models.CharField(verbose_name='производитель', max_length=24, unique=True)
    description = models.TextField(verbose_name='производитель устройства', blank=True)

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'

    def __str__(self):
        return self.name


class ProductResolutions(models.Model):
    name = models.CharField(verbose_name='разрешение', max_length=24, unique=True)
    description = models.TextField(verbose_name='реальное разрешение устройства', blank=True)

    class Meta:
        verbose_name = 'разрешение'
        verbose_name_plural = 'разрешения'

    def __str__(self):
        return self.name


class ProductTypes(models.Model):
    name = models.CharField(verbose_name='тип', max_length=24, unique=True)
    description = models.TextField(verbose_name='описание типа устройства', blank=True)

    class Meta:
        verbose_name = 'тип'
        verbose_name_plural = 'типы'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(ProductCategories, verbose_name='категория', on_delete=models.CASCADE)
    light_source = models.ForeignKey(ProductLightSources, verbose_name='источник света', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(ProductManufacturers, verbose_name='производитель', on_delete=models.CASCADE)
    resolution = models.ForeignKey(ProductResolutions, verbose_name='разрешение', on_delete=models.CASCADE)
    type = models.ForeignKey(ProductTypes, verbose_name='тип', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=64)
    image = models.ImageField(verbose_name='изображение', upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    class Meta:
        verbose_name = 'проектор'
        verbose_name_plural = 'проекторы'

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)
