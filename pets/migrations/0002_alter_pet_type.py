# Generated by Django 3.2.4 on 2021-06-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Cat', 'cat'), ('Dog', 'dog'), ('Parrot', 'parrot')], max_length=6),
        ),
    ]
