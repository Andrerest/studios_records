# Generated by Django 5.1.3 on 2024-11-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_alter_artista_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto',
            field=models.ImageField(blank=True, default='images/default_profile_image.png', upload_to='artistas/'),
        ),
    ]
