# Generated by Django 3.0.8 on 2022-04-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('age', models.IntegerField(verbose_name='age')),
                ('salary', models.DecimalField(decimal_places=10, max_digits=100000000000, verbose_name='salary')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('number', models.IntegerField(verbose_name='number')),
                ('country', models.CharField(max_length=255, verbose_name='country')),
            ],
        ),
        migrations.CreateModel(
            name='sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tasks', models.TextField(default=' ', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=100)),
            ],
        ),
    ]