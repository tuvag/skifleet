# Generated by Django 4.1.3 on 2022-12-10 00:40

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skis', '0002_ski_image_alter_ski_color_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ski',
            name='image',
        ),
        migrations.AlterField(
            model_name='ski',
            name='color_tag',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=[('#66A3BB', 'navy'), ('#FF8C8C', 'pink'), ('#FFBFBF', 'lightpink'), ('#66A3BB', 'blue'), ('#F1FFABC', 'lightgreen'), ('#A8E0A8', 'green')]),
        ),
    ]