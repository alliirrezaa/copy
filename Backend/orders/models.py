from django.db import models
from accounts.models import User
from home.models import Product

class OrderDetail(models.Model):
    userId=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    productId=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="محصول")
    count=models.PositiveIntegerField(verbose_name="تعداد")
    desc=models.TextField(verbose_name="توضیحات")
    price=models.PositiveIntegerField(verbose_name="قیمت")
    name=models.CharField(max_length=100,verbose_name="نام")
    date=models.CharField(max_length=20,verbose_name="تاریخ")
    tracking_code=models.CharField(max_length=8,null=True,verbose_name="کد رهگیری")
    imgfile=models.ImageField(upload_to='formDetail',null=True,blank=True,verbose_name="عکس")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="سفارش"
        verbose_name_plural="سفارشات"