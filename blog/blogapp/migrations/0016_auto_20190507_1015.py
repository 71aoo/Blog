# Generated by Django 2.1.5 on 2019-05-07 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20190507_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.Article'),
        ),
    ]
