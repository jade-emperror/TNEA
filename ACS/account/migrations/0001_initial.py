# Generated by Django 4.0.1 on 2022-02-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(max_length=75)),
                ('pwd', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]