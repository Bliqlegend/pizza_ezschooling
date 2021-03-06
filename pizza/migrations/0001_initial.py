# Generated by Django 2.2.9 on 2020-12-06 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Small', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(default='Onion', max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Square', max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Size')),
                ('toppings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Toppings')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Types')),
            ],
        ),
    ]
