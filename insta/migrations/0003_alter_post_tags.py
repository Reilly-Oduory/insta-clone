# Generated by Django 3.2.5 on 2021-07-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='insta.Tag'),
        ),
    ]