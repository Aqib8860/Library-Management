# Generated by Django 3.2.10 on 2022-05-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_librarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_member',
            field=models.BooleanField(default=True),
        ),
    ]
