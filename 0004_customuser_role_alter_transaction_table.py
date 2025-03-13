# Generated by Django 5.0.4 on 2024-09-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('customer', 'Customer')], default='customer', max_length=10),
        ),
        migrations.AlterModelTable(
            name='transaction',
            table='transaction',
        ),
    ]
