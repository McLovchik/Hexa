# Generated by Django 4.2 on 2023-05-14 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0004_remove_product_stripe_product_price_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
