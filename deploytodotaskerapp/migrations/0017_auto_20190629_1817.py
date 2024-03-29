# Generated by Django 2.1.7 on 2019-06-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploytodotaskerapp', '0016_auto_20190629_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paytmhistory',
            name='CURRENCY',
        ),
        migrations.RemoveField(
            model_name='paytmhistory',
            name='resultStatus',
        ),
        migrations.AddField(
            model_name='paytmhistory',
            name='REFUNDAMT',
            field=models.FloatField(default=0, verbose_name='RFUND AMOUNT'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKNAME',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='BANK NAME'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKTXNID',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='BANK TXN ID'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='GATEWAYNAME',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='GATEWAY NAME'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='ORDERID',
            field=models.CharField(max_length=70, verbose_name='ORDER ID'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='PAYMENTMODE',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='PAYMENT MODE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPCODE',
            field=models.CharField(max_length=20, verbose_name='STATUS'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPMSG',
            field=models.TextField(max_length=600, verbose_name='RESP MSG'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNID',
            field=models.CharField(max_length=70, verbose_name='ORDER ID'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNTYPE',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='TNX TYPE'),
        ),
    ]
