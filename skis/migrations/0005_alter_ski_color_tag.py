# Generated by Django 4.1.3 on 2022-12-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skis', '0004_alter_ski_color_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ski',
            name='color_tag',
            field=models.CharField(default='#66A3BB', max_length=7),
        ),
    ]
