# Generated by Django 3.0.6 on 2020-05-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='botModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=200)),
                ('output', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'bot',
            },
        ),
    ]