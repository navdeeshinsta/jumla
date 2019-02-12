# Generated by Django 2.1.7 on 2019-02-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_on_sale', '0003_pricing_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videopackentity',
            name='video_pack_content_foreign_key',
        ),
        migrations.AlterField(
            model_name='pricing',
            name='pricing_daily_basis',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='pricing_monthly_basis',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='pricing_weekly_basis',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='pricing_yearly_basis',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subscribed',
            name='subscribed_amount',
            field=models.IntegerField(),
        ),
    ]