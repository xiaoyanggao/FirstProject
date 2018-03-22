# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jump_group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('groupname', models.CharField(max_length=30, null=True, verbose_name='\u7ec4\u540d\u79f0', blank=True)),
                ('dev_list', models.CharField(max_length=9999, null=True, verbose_name='\u673a\u5668', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u673a\u5668\u5206\u7ec4\u8868',
                'verbose_name_plural': '\u673a\u5668\u5206\u7ec4\u8868',
            },
        ),
        migrations.CreateModel(
            name='Jump_logs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField(null=True, verbose_name='IP', blank=True)),
                ('file_path', models.CharField(max_length=30, null=True, verbose_name='\u65e5\u5fd7\u6587\u4ef6\u8def\u5f84', blank=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('username', models.ForeignKey(verbose_name='\u7528\u6237\u540d', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u65e5\u5fd7\u8868',
                'verbose_name_plural': '\u65e5\u5fd7\u8868',
            },
        ),
        migrations.CreateModel(
            name='Jump_Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe9\x80\x9a\xe7\x9f\xa5\xe5\x86\x85\xe5\xae\xb9')),
                ('status', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u901a\u77e5\u8868',
                'verbose_name_plural': '\u901a\u77e5\u8868',
            },
        ),
        migrations.CreateModel(
            name='Jump_prem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(verbose_name='\u7ed1\u5b9a\u7ec4', blank=True, to='jump.Jump_group', null=True)),
                ('username', models.ForeignKey(verbose_name='\u7528\u6237\u540d', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6743\u9650\u7ed1\u5b9a\u8868',
                'verbose_name_plural': '\u7528\u6237\u6743\u9650\u7ed1\u5b9a\u8868',
            },
        ),
        migrations.CreateModel(
            name='Jump_user',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30, null=True, verbose_name='\u8d26\u6237\u540d\u79f0', blank=True)),
                ('password', models.CharField(max_length=30, null=True, verbose_name='\u8d26\u6237\u5bc6\u7801', blank=True)),
                ('permiss', models.TextField(verbose_name='sudo\u6743\u9650')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u8fdc\u7a0b\u8d26\u6237\u8868',
                'verbose_name_plural': '\u8fdc\u7a0b\u8d26\u6237\u8868',
            },
        ),
        migrations.AddField(
            model_name='jump_group',
            name='user',
            field=models.ForeignKey(verbose_name='\u7ed1\u5b9a\u8d26\u53f7', blank=True, to='jump.Jump_user', null=True),
        ),
    ]
