# Generated by Django 4.1.4 on 2023-02-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_offers_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='discount',
            field=models.PositiveIntegerField(),
        ),
    ]
