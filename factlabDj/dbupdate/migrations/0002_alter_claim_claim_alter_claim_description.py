# Generated by Django 4.0.2 on 2022-05-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbupdate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='claim',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]