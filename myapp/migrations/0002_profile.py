# Generated by Django 3.0 on 2024-09-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PROFILE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('Open_Time', models.CharField(max_length=100)),
                ('Close_Time', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('estDate', models.DateField()),
            ],
        ),
    ]
