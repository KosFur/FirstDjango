# Generated by Django 4.2.11 on 2024-08-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_color_item_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color_code',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]
