from django.db import models

# Create your models here.


class Category(models.Model):
    cat_id = models.IntegerField()
    category_name = models.CharField(max_length = 100)
    category_image = models.ImageField(upload_to = 'category_images', null = True, blank = True)
    status = models.BooleanField(default = True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return str(self.category_name)

class Product(models.Model):
    prod_id = models.IntegerField()
    category_id = models.IntegerField()
    quantity = models.IntegerField()
    name = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to = 'product_images', null= True, blank = True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = False)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
    
    def __str__(self):
        return str(self.name)


