# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categories',
            field=models.ManyToManyField(to='users.Category'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='category',
            name='users',
        ),
        migrations.AlterField(
            model_name='user',
            name='anniversaryDate',
            field=models.DateField(verbose_name=b'anniversaryDate'),
        ),
    ]
