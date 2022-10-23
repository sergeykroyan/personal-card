# Generated by Django 4.1.2 on 2022-10-22 22:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F')], default='Male', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccinated', models.CharField(choices=[('Yes', 'Y'), ('No', 'N')], default='No', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField(default=16, validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(122)])),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card.gender')),
                ('vaccinated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card.vaccination')),
            ],
        ),
    ]