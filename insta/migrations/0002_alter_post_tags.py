# Generated by Django 3.2.5 on 2021-07-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='insta.Tag'),
        ),
    ]
