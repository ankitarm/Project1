from django.db import models

# Create your models here.

class Product(models.Model):
    productid = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name



class Order(models.Model):
    detail_id = models.AutoField(primary_key=True)
    inputname = models.CharField(max_length=50)
    inputEmail4 = models.CharField(max_length=50, default="")
    inputAddress = models.CharField(max_length=50, default="")
    inputAddress2 = models.CharField(max_length=300, default="")
    inputCity = models.CharField(max_length=50, default="")
    inputState = models.CharField(max_length=50, default="")
    inputZip = models.CharField(max_length=50, default="")
    phone= models.CharField(max_length=50, default="")

    def __str__(self):
        return self.inputname
