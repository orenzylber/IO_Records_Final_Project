# Generated by Django 4.2.2 on 2023-07-22 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0015_alter_cart_totalamount_alter_order_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='addressLine1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='addressLine2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='firstName',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='lastName',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
    ]
