# Generated by Django 3.0.3 on 2020-03-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('routeName', models.CharField(max_length=100)),
                ('busNumber', models.IntegerField()),
                ('StopName', models.ManyToManyField(to='route.Stop')),
            ],
        ),
    ]