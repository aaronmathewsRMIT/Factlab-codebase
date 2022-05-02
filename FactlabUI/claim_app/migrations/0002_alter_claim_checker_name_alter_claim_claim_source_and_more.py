# Generated by Django 4.0.2 on 2022-05-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='checker_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='claim_source',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='claimant',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='media_link_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='media_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='party',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='project',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='source_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='sub_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='topic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='verdict',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='verdict_simplified',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='who_lodged_info',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
