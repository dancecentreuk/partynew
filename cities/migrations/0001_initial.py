# Generated by Django 2.2.3 on 2019-10-04 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the City name', max_length=200)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('venue_phone', models.CharField(blank=True, max_length=20)),
                ('venue_coordinator', models.CharField(blank=True, max_length=200)),
                ('venue_email', models.CharField(blank=True, max_length=300)),
                ('venue_website', models.URLField(blank=True)),
                ('capacity', models.IntegerField(blank=True)),
                ('cost', models.IntegerField(blank=True)),
                ('no_studios', models.IntegerField(default=1)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/venue/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/venue/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/venue/%Y/%m/%d/')),
                ('notes', models.TextField(blank=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cities.City')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_name', models.CharField(help_text='Enter Studio or website name', max_length=200)),
                ('studio_website', models.URLField(blank=True)),
                ('studio_email', models.CharField(help_text='Enter Studio contact', max_length=200)),
                ('studio_mobile', models.CharField(help_text='Enter contact number', max_length=15)),
                ('studio_contact', models.CharField(default='James Cooke', max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cities.City')),
            ],
        ),
    ]
