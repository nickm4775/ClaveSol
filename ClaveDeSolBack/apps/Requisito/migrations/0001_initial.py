# Generated by Django 4.2.6 on 2024-04-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('permanecer', models.BooleanField()),
                ('subir', models.BooleanField()),
            ],
        ),
    ]
