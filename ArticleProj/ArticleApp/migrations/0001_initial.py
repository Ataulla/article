# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publication_date', models.DateTimeField(verbose_name=b'publication date')),
                ('category', models.CharField(max_length=200)),
                ('hero_image_name', models.CharField(max_length=200)),
                ('optional_image_name', models.CharField(max_length=200)),
                ('body_text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
