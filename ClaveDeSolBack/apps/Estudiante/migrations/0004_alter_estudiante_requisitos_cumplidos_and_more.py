# Generated by Django 4.2.6 on 2024-04-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requisito', '0001_initial'),
        ('Estudiante', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='requisitos_cumplidos',
            field=models.ManyToManyField(blank=True, related_name='estudiantes_cumplieron', to='Requisito.requisito'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='requisitos_cumplidos_permanecer',
            field=models.ManyToManyField(blank=True, related_name='estudiantes_cumplieron_permanecer', to='Requisito.requisito'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='requisitos_cumplidos_subir',
            field=models.ManyToManyField(blank=True, related_name='estudiantes_cumplieron_subir', to='Requisito.requisito'),
        ),
    ]
