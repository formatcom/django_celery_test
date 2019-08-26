# Generated by Django 2.2.4 on 2019-08-26 18:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_id', models.CharField(max_length=255)),
                ('output', models.IntegerField(null=True)),
            ],
        ),
    ]
