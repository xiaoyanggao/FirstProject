#!/bin/bash
echo '初始化数据库表和登陆账户'
python manage.py makemigrations
python manage.py migrate
