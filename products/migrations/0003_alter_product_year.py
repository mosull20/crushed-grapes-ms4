# Generated by Django 4.0.1 on 2022-02-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]