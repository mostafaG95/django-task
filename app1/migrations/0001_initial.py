# Generated by Django 4.1.4 on 2022-12-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='photo/%y/%m/%d')),
                ('description', models.TextField(max_length=100)),
                ('model', models.CharField(choices=[(2010, 2010), (2015, 2015), (2020, 2020)], max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
