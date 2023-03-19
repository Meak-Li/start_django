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