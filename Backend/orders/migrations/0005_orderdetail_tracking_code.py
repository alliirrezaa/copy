# Generated by Django 4.0.5 on 2022-06-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_orderdetail_tracking_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='tracking_code',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
