# Generated by Django 5.1.3 on 2025-02-27 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_orders_orderupdate_alter_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
