# Generated by Django 4.2.4 on 2023-09-29 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_club_vote_ratio_club_votes_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
