# Generated by Django 4.2.1 on 2023-05-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]