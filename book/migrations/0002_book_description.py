# Generated by Django 3.2.10 on 2022-05-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]