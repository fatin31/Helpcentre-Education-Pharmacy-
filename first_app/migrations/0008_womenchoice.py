# Generated by Django 3.0.14 on 2023-05-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_babycare'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=2083)),
            ],
        ),
    ]
