# Generated by Django 3.0.7 on 2020-07-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
