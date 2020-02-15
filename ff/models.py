from django.db import models
# import calendar   

shoeSizesUS = [(5.0, "US 5.0"), (5.5, "US 5.5"), (6.0, "US 6.0"), (6.5, "US 6.5"), (7.0, "US 7.0"), (7.5, "US 7.5"), (8.0, "US 8.0"), (8.5, "US 8.5"), (9.0, "US 9.0"), (9.5, "US 9.5"), (10.0, "US 10.0"), (10.5, "US 10.5"), (11.0, "US 11.0"), (11.5, "US 11.5"), (12.0, "US 12.0"), (13.0, "US 13.0"), (14.0, "US 14.0"), (15.0, "US 15.0"), (16.0, "US 16.0")]

# class Apparel(models.Model):
#     shoe = 

#     def __str__(self):
#         return f'{self.course} - {(self.courseCode)}'

class Shoe(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=150, default='Shoe Type', blank=False, unique=True)
    brand = models.CharField(max_length=80, default='Brandless', blank=False, unique=True)
    desc = models.TextField(max_length=400)
    thumbnail1 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')
    thumbnail2 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')
    thumbnail3 = models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')
    size = models.DecimalField(max_digits=3, decimal_places=1, choices=shoeSizesUS)
    

    def __str__(self):
        return f'{self.title}'

# class Captions(models.Model):
#     course 
