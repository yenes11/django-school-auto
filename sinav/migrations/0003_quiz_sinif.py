# Generated by Django 3.1.7 on 2021-05-18 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('sinav', '0002_auto_20210512_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='sinif',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='users.siniflar'),
        ),
    ]
