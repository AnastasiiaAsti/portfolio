# Generated by Django 4.0.4 on 2022-07-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name='post date')),
                ('details', models.CharField(max_length=2000)),
            ],
        ),
    ]
