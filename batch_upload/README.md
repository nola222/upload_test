##### python manage.py runserver报错 +1
```python
  File "manage.py", line 16
    ) from exc
         ^
SyntaxError: invalid syntax
```
```python
# 使用python3
python3 manage.py runserver
```

##### python3 manage.py runserver报错 +1
```python
  File "E:\env\django_images\lib\site-packages\django\db\backends\mysql\base.py", line 37, in <module>
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.

LookupError: No installed app with label 'admin'.
```
```
# 找到django下的base文件
E:\env\django_images\Lib\site-packages\django\db\backends\mysql\base.py

# 注释35 36行
if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```

##### python3 manage.py runserver报错 +2
```python
  File "E:\env\django_images\lib\site-packages\django\db\backends\mysql\operations.py", line 147, in last_executed_query
    query = query.decode(errors='replace')
AttributeError: 'str' object has no attribute 'decode'
```
```python
# 找到operations文件
E:\env\django_images\Lib\site-packages\django\db\backends\mysql\operations.py

# 修改146行decode为encode
# query = query.decode(errors='replace')
query = query.encode(errors='replace')
```

##### python3 manage.py runserver 成功