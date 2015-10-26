# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 11, 31, 10, 704011, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 11, 31, 16, 71716, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
