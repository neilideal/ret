# Generated by Django 5.1.2 on 2024-10-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, unique_for_date='publish'),
        ),
    ]
