# Generated by Django 3.0.5 on 2021-05-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=10)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
    ]
