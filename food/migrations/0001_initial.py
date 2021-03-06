# Generated by Django 3.0 on 2019-12-14 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name :')),
                ('phone', models.CharField(max_length=50, verbose_name='Number :')),
                ('address', models.CharField(max_length=50, verbose_name='Adrress :')),
                ('logo', models.ImageField(upload_to='logo_image', verbose_name='Logo :')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug :')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User :')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
            },
        ),
    ]
