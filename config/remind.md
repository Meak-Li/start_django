### 可以直接生成一个requirement的安装包文件
~~~
pip freeze > requirements.txt
~~~

## Model
### 逆向生成一个表, 先有表，然后需要生成对应的model
~~~ 
python manage.py inspectdb > model_app/models.py
~~~
### 字段
~~~
BooleanField, CharField, ....官网上面有
UUIDField(primary_key=True, defult=uuid.uuid4) 唯一
~~~

### 测试模型的方法
~~~
python manage.py shell
~~~

## 添加模型数据
~~~
1. django直接创建 
Model.objects.create(filed)

2. 先创建类，然后执行save()方法
obj = Place(name='xxx')
obj.save()     # 可以使用python manage.py shell 测试测试

3. 一对一，一对多 的时候，外键创建数据的时候，外键传入创建的时候，对应的是类名
obj = Person(name='xx', goup=g1)  g1为一个对象

4. 多对多的时候，需要使用set方法
~~~

## model数据的查询
### 查询方式
~~~
1. Model.objects.get() 返回一个对象，没有的时候会报错,返回太多的时候也会报错
2. Model.objects.all()  返回一个QuerySet，里面包含所有的数据
3. Model.objects.filter()  返回一个QuerySet，可以设置查询参数，包含这些规则的数据
4. Model.objects.exclude()  返回一个新的QuerySet，不包含这些规则的数据
~~~
~~~
Waiter.objects.get(name='xx')
Waiter.objects.get(pk='xx')  # pk相当于id
Waiter.objects.all()
Waiter.objects.filter(induction="2023-6-6")
Waiter.objects.filter(induction="2023-6-6").filter(name='xx')  # 可以链式过滤
Waiter.objects.filter(induction="2023-6-6", name='xx' )  # 可以链式过滤
Waiter.objects.exclude(induction="2023-6-6") # 相当于上一条数据的取反
~~~
### 数据的条件查询
~~~
exact ：判断是否等于value，一般不使用，而直接使用 '='
contains：是否包含,大小写敏感，如果需要不敏感的话，使用icontains
startswith：以value开头,大小写敏感
endwith：以value结尾,大小写敏感 
in：是否包含在范围内
isnull：是否为null， 如：filter(name__isnull=Flase)
gt：大于，如：filter(sage__gt=30) ， 年龄大于30
gte：大于等于
lt：小于
lte：小于等于
~~~
~~~
Waiter.objects.filter(id_exact=6)
Waiter.objects.filter(id=6)
Waiter.objects.filter(name__contains='张')
Waiter.objects.filter(name__startswith='袁')
Waiter.objects.filter(name__endswith='了')
Waiter.objects.filter(name__in=['关羽', '黄忠'])
Waiter.objects.filter(name__isnull=True)
Waiter.objects.filter(id__gte=5)  # 大于等于
Waiter.objects.filter(id__lt=6)   # 小于
Waiter.objects.filter(id__lte=6)  # 小于等于

外键的时候
Waiter.objects.filter(restaurant=1)  # 后面写id
Waiter.objects.filter(restaurant_id=1)
Waiter.objects.filter(restaurant__name="肯德基")  # 使用的外键的字段(__xx)
~~~
### 时间查询
~~~
Waiter.objects.filter(induction="2023-6-6 00:00:00")
Waiter.objects.filter(induction__date="2023-6-6") # 某一天
Waiter.objects.filter(induction__lt="2023-6-6") # 某一天之前
Waiter.objects.filter(induction__date__range=("2023-6-1","2023-6-6")) # 某一个字段
Waiter.objects.all()[:5] # 前五条数据，切片不能倒着获取
~~~
### 排序
~~~
Waiter.objects.all().order_by('-id') # 降序，id排序
Waiter.objects.all().order_by('-id').reverse()  # 反序
Waiter.objects.all().order_by('induction')
Waiter.objects.all().order_by('induction', '-id')
Waiter.objects.all().count()
Waiter.objects.all().values('id', 'name')  # 返回指定的字段
~~~
### 关联查询
~~~
一对一：（正查与反查都是一样的）
p1 = Place.objects.first()
p1.reatrurant
一对多, 多对多查询的时候：
1. 从有索引关系的一方查询没有索引的一方：直接使用字段名查找
2. 从没有索引的一方查询有索引的一方，使用对应的模型名_set查找
~~~
### 聚合查询 使用aggregate函数一起使用
~~~
Cook.objects.aggregate(Max('age'))  # {'age__max':30}
Cook.objects.aggregate(a_min=Max('age'))  # 重命名  {'a_min':30}
Cook.objects.aggregate(Max('age'), Min('age'), Avg('age'), Sum('age'))
~~~
### 分组查询 使用values()，annotate()一起使用，顺序不能颠倒
~~~
Cook.objects.values('sect').annotate(Min('level')).filter(sect='xx')
Cook.objects.filter(sect='xx').values('sect').annotate(Min('level'))
~~~
## 修改数据
1. 先获取对象，通过对象的属性更新数据，在保存（更新单条数据）
2. 通过QuerySet的update函数来更新数据（更新多条数据）
~~~
1.
    c = Cook.objects.get(pk=1)
    c.name = 'xxx'
    c.save()
2.
    Cook.objects.filter(sect='xx').update(level=8)
~~~
### 刷新数据
~~~
c = Cook.objects.get(pk=1)
c.refresh_from_db()
~~~