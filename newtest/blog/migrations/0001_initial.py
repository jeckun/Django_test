# Generated by Django 2.2.2 on 2019-07-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('desc', models.CharField(max_length=1000, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='正文')),
            ],
        ),
    ]
