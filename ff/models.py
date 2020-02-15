from django.db import models
# import calendar   

# shoeSizesUS = [(5.0, "US 5.0"), (5.5, "US 5.5"), (6.0, "US 6.0"), (6.5, "US 6.5"), (7.0, "US 7.0"), (7.5, "US 7.5"), (8.0, "US 8.0"), (8.5, "US 8.5"), (9.0, "US 9.0"), (9.5, "US 9.5"), (10.0, "US 10.0"), (10.5, "US 10.5"), (11.0, "US 11.0"), (11.5, "US 11.5"), (12.0, "US 12.0"), (13.0, "US 13.0"), (14.0, "US 14.0"), (15.0, "US 15.0"), (16.0, "US 16.0")]
shoeSizesUS = [(8.0, "US 8.0"), (8.5, "US 8.5"), (9.0, "US 9.0"), (9.5, "US 9.5"), (10.0, "US 10.0"), (10.5, "US 10.5"), (11.0, "US 11.0"), (11.5, "US 11.5"), (12.0, "US 12.0")]

class ProductType(models.Model):
    typeName = models.CharField(max_length=50, default='Product Type', blank=False, unique=True)

    def __str__(self):
        return f'{self.typeName}'

class Shoe(models.Model):
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='shoeptype')
    name = models.CharField(max_length=150, default='Shoe Type', blank=False, unique=True)
    brand = models.CharField(max_length=80, default='Brandless')
    desc = models.TextField(max_length=400)
    thumbnail1 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')
    thumbnail2 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')
    thumbnail3 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')
    # size = models.DecimalField(max_digits=3, decimal_places=1, choices=shoeSizesUS)

    qtyin = models.PositiveSmallIntegerField(default="10")
    usSize8_0 = models.BooleanField(default=True)
    usSize8_5 = models.BooleanField(default=True)
    usSize9_0 = models.BooleanField(default=True)
    usSize9_5 = models.BooleanField(default=True)
    usSize10_0 = models.BooleanField(default=True)
    usSize10_5 = models.BooleanField(default=True)
    usSize11_0 = models.BooleanField(default=True)
    usSize11_5 = models.BooleanField(default=True)
    usSize12_0 = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.name}'

    # def clean(self, *args, **kwargs):
    #     from ff.models import Shoe
    #     # x = self.pk
    #     for i in range(10):
    #         q = Shoe.objects.create(productType = self.productType, name = ("nike af1 - " + str(i) ), brand = self.brand, desc = self.desc, thumbnail1 = self.thumbnail1, thumbnail2 = self.thumbnail2, thumbnail3 = self.thumbnail3)

class Skirt(models.Model):
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='skirtptype')
    name = models.CharField(max_length=150, default='Skirt Type', blank=False, unique=True)
    brand = models.CharField(max_length=80, default='Brandless')
    desc = models.TextField(max_length=400)
    thumbnail1 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/skirt')
    thumbnail2 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/skirt')
    thumbnail3 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/skirt')

class Bag(models.Model):
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='bagptype')
    name = models.CharField(max_length=150, default='Bag Type', blank=False, unique=True)
    brand = models.CharField(max_length=80, default='Brandless')
    desc = models.TextField(max_length=400)
    thumbnail1 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/bags')
    thumbnail2 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/bags')
    thumbnail3 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/bags')

# class Captions(models.Model):
#     course 


# def dup(sender, instance, **kwargs):
#     daysCount = instance.operatingHrs.all()
#     if daysCount.count() == 0:
#         for i in range(5):
#             q = operatingHours.objects.create(stall=instance, day=i, opening=800, closing=1700)
#         q = operatingHours.objects.create(stall=instance, day=5, opening=0, closing=0)
#         q = operatingHours.objects.create(stall=instance, day=6, opening=0, closing=0)
# post_save.connect(dup, sender=Shoe)