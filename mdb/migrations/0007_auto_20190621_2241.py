# Generated by Django 2.2.2 on 2019-06-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdb', '0006_auto_20190611_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
