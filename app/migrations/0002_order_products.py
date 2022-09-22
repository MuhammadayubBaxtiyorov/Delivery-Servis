# Generated by Django 4.0.6 on 2022-08-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(auto_now_add=True, choices=[('car', 'car'), ('moto', 'moto')], null=True)),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('eat', 'eat'), ('drink', 'drink'), ('gadjets', 'gadjets')], max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
