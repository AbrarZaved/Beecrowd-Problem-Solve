# Generated by Django 4.2.4 on 2023-10-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_club_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='Image',
            field=models.ImageField(default='user.png', height_field=50, upload_to='static/images', width_field=50),
        ),
    ]
