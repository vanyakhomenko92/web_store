# Generated by Django 2.2.5 on 2020-12-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productimage_is_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категорія товару',
                'verbose_name_plural': 'Категорії товарів',
            },
        ),
    ]
