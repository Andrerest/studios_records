# Generated by Django 5.1.3 on 2024-11-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='precio_entrada',
            new_name='entrada_general',
        ),
        migrations.AddField(
            model_name='evento',
            name='ciudad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='direccion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='entrada_vip',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Precio de entrada al evento. Déjelo en 0 para eventos gratuitos.', max_digits=10),
        ),
        migrations.AddField(
            model_name='evento',
            name='pais',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='ubicacion',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
