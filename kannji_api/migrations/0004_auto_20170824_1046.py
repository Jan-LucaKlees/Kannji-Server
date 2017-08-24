# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kannji_api', '0003_auto_20170411_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiragana',
            fields=[
                ('kana_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('literal', models.CharField(max_length=1)),
                ('transliteration', models.CharField(max_length=4)),
                ('type', models.CharField(choices=[('MO', 'Monograph'), ('DC', 'Diacritic'), ('DG', 'Digraph'), ('DD', 'Diacritic-Digraph')], max_length=2)),
                ('corresponding_katakana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kannji_api.Katakana')),
                ('diacritic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diacritic_uuid', to='kannji_api.Hiragana')),
                ('digraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digraph_uuid', to='kannji_api.Hiragana')),
                ('monograph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monograph_uuid', to='kannji_api.Hiragana')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Katakana',
            fields=[
                ('kana_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('literal', models.CharField(max_length=1)),
                ('transliteration', models.CharField(max_length=4)),
                ('type', models.CharField(choices=[('MO', 'Monograph'), ('DC', 'Diacritic'), ('DG', 'Digraph'), ('DD', 'Diacritic-Digraph')], max_length=2)),
                ('corresponding_hiragana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kannji_api.Hiragana')),
                ('diacritic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diacritic_uuid', to='kannji_api.Katakana')),
                ('digraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digraph_uuid', to='kannji_api.Katakana')),
                ('monograph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monograph_uuid', to='kannji_api.Katakana')),
            ],
            options={
                'abstract': False,
            },
        )
    ]
