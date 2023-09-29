# Generated by Django 4.2.4 on 2023-09-23 08:11

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_guestqty_product_delete_guest_delete_guestqty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestname', models.CharField(max_length=100)),
                ('guestid', models.CharField(max_length=100)),
                ('guestPrescriptionImage', models.ImageField(upload_to=app.models.getguestPrescriptionCartFileName)),
                ('email', models.CharField(max_length=50)),
                ('mobileno', models.CharField(max_length=50)),
                ('totalprice', models.IntegerField(default=0)),
                ('totalproducts', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'Apply'), (2, 'Dispatched'), (3, 'Out For Delivery'), (4, 'Delivered'), (5, 'Declined')], default=1)),
                ('address', models.TextField(max_length=300)),
                ('pincode', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuestQty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('guestid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.guest')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]