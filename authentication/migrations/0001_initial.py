# Generated by Django 4.0.2 on 2022-03-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=122)),
                ('psummary', models.CharField(max_length=122)),
                ('pdescription', models.CharField(max_length=122)),
                ('products', models.CharField(max_length=122)),
                ('kanalysis', models.CharField(max_length=122)),
                ('kinsisghts', models.CharField(max_length=122)),
                ('tags', models.CharField(max_length=122)),
                ('owner', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
