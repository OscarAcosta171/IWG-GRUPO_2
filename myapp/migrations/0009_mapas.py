# Generated by Django 4.2.6 on 2023-12-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_marker_color_marker_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mapas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapa', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]
