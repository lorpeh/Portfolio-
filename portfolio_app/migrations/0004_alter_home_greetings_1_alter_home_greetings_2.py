# Generated by Django 4.1.1 on 2022-09-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_rename_porfolio_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(max_length=30),
        ),
    ]
