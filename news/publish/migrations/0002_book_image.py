# Generated by Django 3.0.7 on 2020-07-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='Null', upload_to='images/'),
        ),
    ]
