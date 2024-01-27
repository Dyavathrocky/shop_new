from django.db import models

# Create your models here.

class Category(models.Model):
    """Class to represent the name and slug for product"""
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        """to pass the metadata values from previous class and used for index"""
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    """this is for product class model"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name="products")
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    descripion = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avilable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        """this is for meta data class"""
        ordering = ['name']
        indexes = [models.Index(fields=['id','slug']),
                   models.Index(fields=['name']),
                   models.Index(fields=['-created']),]
        
    def __str__(self):
        return self.name
