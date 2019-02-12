# Generated by Django 2.1.7 on 2019-02-12 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos_on_sale', '0004_auto_20190212_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addons_content_id', models.IntegerField()),
                ('addon_price', models.IntegerField()),
                ('addon_duration', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscribed',
            name='id',
        ),
        migrations.AddField(
            model_name='subscribed',
            name='subscribed_id',
            field=models.AutoField(default=-1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contententity',
            name='video_foreign_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videos_on_sale.VideoEntity'),
        ),
        migrations.AlterField(
            model_name='contententity',
            name='video_pack_foreign_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videos_on_sale.VideoPackEntity'),
        ),
        migrations.AddField(
            model_name='addons',
            name='addons_for_content_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos_on_sale.ContentEntity'),
        ),
    ]
