import django.utils.dateformat
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    img = models.ImageField(upload_to='uploads',default='DEFAULT VALUE')


    def __str__(self):
        return self.name


class Sub_category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    sub_name = models.CharField(max_length=30, blank=False, null=False)
    img = models.ImageField(upload_to='uploads', default='DEFAULT VALUE')


    def __str__(self):
        return self.sub_name




class All_products(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE, null=True)
    all_name = models.CharField(max_length=30,blank=False,null=False)
    img = models.ImageField(upload_to='pictures',blank=False,null=False)
    description = models.TextField(max_length=500,blank=True,null=True)
    price = models.IntegerField(null=False, blank=False)
    discount_p = models.FloatField(null=True, blank=True)
    stock= models.IntegerField()

    date_upload = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.all_name


class Cart(models.Model):
    cart_id = models.CharField(max_length=250,unique=True)
    date_add = models.DateTimeField(auto_now_add=True)


class Items(models.Model):
    products = models.ForeignKey(All_products,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def Total(self):
        return  self.products.discount_p*self.quantity

    # def Ftotal(self):
    #
    #     return  (self.products.discount_p*self.quantity)+45


class Userlist(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    age = models.IntegerField()
    pic = models.ImageField(upload_to="Userimg")

    def __str__(self):
        return self.name