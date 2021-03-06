# Generated by Django 4.0.4 on 2022-04-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Reservation')),
                ('check_in', models.DateField(verbose_name='Check in')),
                ('checkout', models.DateField(verbose_name='Checkout')),
                ('flat', models.CharField(max_length=65, verbose_name='Flat')),
                ('city', models.CharField(max_length=28, verbose_name='City')),
                ('net_incoming', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Net incoming')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Commission',
                'verbose_name_plural': 'Commissions',
                'ordering': ('-created_at',),
            },
        ),
    ]
