# Generated by Django 3.1.5 on 2021-01-23 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('food', models.CharField(max_length=100, verbose_name='name food')),
                ('type_food', models.CharField(max_length=100, verbose_name='type food')),
                ('stock', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Delivey_Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('quantity', models.CharField(max_length=100, verbose_name='amount of food')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(blank=True)),
                ('delivery_food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.food')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
