#!/bin/bash
echo '初始化数据库表和登陆账户'
python manage.py makemigrations
python manage.py migrate
echo "from Integrated.models import UserProfile as User; User.objects.create_superuser(username='yangxu', email='yangxu1@kingsoft.com', password='a8556432')" | python manage.py shell

echo "账号、密码：yangxu1@kingsoft.com/a8556432"
