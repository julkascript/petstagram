# Generated by Django 3.1.3 on 2020-11-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20201126_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to='pets'),
        ),
    ]
