# Generated by Django 3.2.8 on 2021-11-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='Account',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
