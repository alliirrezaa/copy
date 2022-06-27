from django.db import models

class faq(models.Model):
    question=models.CharField(max_length=150)
    answer=models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name="پرسش های متداول"
        verbose_name_plural="پرسش های متداول"

class Category(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub_cat',verbose_name="زیر دسته")
    sub=models.BooleanField(default=False,verbose_name="زیر دسته")
    name=models.CharField(max_length=200,verbose_name="نام")
    create=models.DateTimeField(auto_now_add=True,verbose_name="ایجاد")
    update=models.DateTimeField(auto_now=True,verbose_name="به روزرسانی")
    image=models.ImageField(upload_to='category',null=True,blank=True,verbose_name="عکس")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"

class Product(models.Model):
    category=models.ManyToManyField(Category,verbose_name="دسته بندی")
    name=models.CharField(max_length=200,verbose_name="نام")
    information=models.TextField(blank=True,null=True,verbose_name="توضیحات")
    price=models.PositiveIntegerField(verbose_name="قیمت")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"

"""class Forms(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    store_name=models.CharField(max_length=100,blank=True)
    job=models.CharField(max_length=100,blank=True)
    management=models.CharField(max_length=100,blank=True)
    media_address=models.CharField(max_length=100,blank=True)
    mobile=models.IntegerField(default=1,blank=True)
    landline=models.IntegerField(default=1,blank=True)
    quantity=models.PositiveIntegerField(default=0,blank=True)
    material=models.CharField(max_length=100,blank=True)
    information=models.TextField(blank=True)
    length=models.PositiveIntegerField(default=10,blank=True)
    width=models.PositiveIntegerField(default=10,blank=True)"""