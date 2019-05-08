# Generated by Django 2.1.5 on 2019-04-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_navbar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('content', models.TextField(max_length=20000000000000000)),
                ('tags', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('change_time', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]