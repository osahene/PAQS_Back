# Generated by Django 3.1.2 on 2021-01-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0003_remove_prodqrgen_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodqrgen',
            name='qty',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]