from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=32, verbose_name='地名')
    address = models.CharField(max_length=64, null=True, verbose_name='地名')

    class Meta:
        db_table = 'shop_place'


class Restaurant(models.Model):
    name = models.CharField(max_length=32, verbose_name='餐厅名')
    place = models.OneToOneField(Place, on_delete=models.CASCADE, verbose_name="所在位置", null=True)

    class Meta:
        db_table = 'shop_restaurant'


class Waiter(models.Model):
    name = models.CharField(max_length=32, verbose_name='服务员名字')
    induction = models.DateTimeField(verbose_name='入职时间', null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='所属餐厅', null=True)

    class Meta:
        db_table = 'shop_waiter'


class Food(models.Model):
    name = models.CharField(max_length=32, verbose_name='食物名字')
    is_main = models.BooleanField(verbose_name='是否是主食', default=False, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='所属餐厅', null=True)

    class Meta:
        db_table = 'shop_food'
