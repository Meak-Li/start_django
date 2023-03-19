from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.CharField(max_length=32)

    class Meta:
        db_table = 't_user'  # 表数据库里面名称


class PLace(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)

    class Meta:
        db_table = 't_place'


class Restaurant(models.Model):
    palace = models.OneToOneField(PLace, on_delete=models.CASCADE, primary_key=True)
    servers_hot = models.BooleanField(default=False)
    servers_cool = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 't_restaurant'


class SchoolClass(models.Model):
    name = models.CharField(max_length=32)


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    school_class = models.ManyToManyField(SchoolClass)  # 会自动生成第三方表， 自定义的时候需要新建一个第三方表，并且里面有两个外键，还需要建立一个多对多的字段


# 自定义第三方的表，多对多表设计
class Person(models.Model):
    name = models.CharField(max_length=32)


class Language(models.Model):
    name = models.CharField(max_length=32)
    person_language = models.ManyToManyField(
        Person,
        through='PersonLanguage',
        through_fields=('language', 'person')  # 当第三方表里面存在多个外键的时候，需要指定，多对多需要关联的是哪两个表，且其他的表需要指定related_name字段
    )


class PersonLanguage(models.Model):
    LEVEL = (
        (1, 'A'),
        (2, 'B'),
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Person, on_delete=models.CASCADE,
                                   related_name="restaurant_person")  # related_name反向引用的名字
    level = models.CharField(choices=LEVEL, max_length=32)  # 可选字段的写法


# 自关联model，主要用于地区之间的关联，评论与回复等等地方
class Area(models.Model):
    name = models.CharField(max_length=32)
    pid = models.ForeignKey('self', on_delete=models.CASCADE)  # 一对多的关系，省，市，区


class Persons(models.Model):
    friends = models.ManyToManyField('self')  # 多对多的关系，主播与粉丝的关系，链接与友情链接



