# Generated by Django 2.2.17 on 2020-12-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0004_auto_20201202_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Other',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='skills',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
