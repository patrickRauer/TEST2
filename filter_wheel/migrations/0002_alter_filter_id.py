# Generated by Django 3.2.9 on 2021-11-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_wheel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]