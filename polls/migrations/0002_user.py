# Generated by Django 5.0.4 on 2024-09-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
