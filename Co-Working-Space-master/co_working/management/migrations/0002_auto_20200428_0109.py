# Generated by Django 3.0.5 on 2020-04-27 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=255)),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=3, default='0', max_digits=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer_shop',
            name='customer_user_id',
        ),
        migrations.RemoveField(
            model_name='customer_shop',
            name='shop_shop_id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='table',
            name='order_order_id',
        ),
        migrations.RemoveField(
            model_name='table',
            name='shop_shop_id',
        ),
        migrations.RemoveField(
            model_name='wallet_wallet',
            name='transfer_id',
        ),
        migrations.RemoveField(
            model_name='wallet_wallet',
            name='wallet_wallet_id',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_pic',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='order_list',
            old_name='menu_menu_id',
            new_name='menu_id',
        ),
        migrations.RenameField(
            model_name='order_list',
            old_name='order_order_id',
            new_name='order_id',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='history',
        ),
        migrations.AddField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_price',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=8),
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('in shop', 'in shop'), ('back home', 'back home')], default='in shop', max_length=12),
        ),
        migrations.AddField(
            model_name='order',
            name='reserved_table',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='order',
            name='status_type',
            field=models.CharField(choices=[('not_arrival', 'not arrival'), ('arrived', 'arrived'), ('finished', 'finished')], default='arrived', max_length=12),
        ),
        migrations.AddField(
            model_name='shop',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('close', 'close')], default='open', max_length=5),
        ),
        migrations.AddField(
            model_name='shop',
            name='total_table',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'admin'), ('customer', 'customer'), ('shop', 'shop')], default='customer', max_length=8),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Customer_Shop',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.DeleteModel(
            name='Transfering',
        ),
        migrations.DeleteModel(
            name='wallet_wallet',
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet_id_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Wallet'),
        ),
        migrations.AddField(
            model_name='comment',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Shop'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
