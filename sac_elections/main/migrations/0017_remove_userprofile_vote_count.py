# Generated by Django 3.1.1 on 2020-09-05 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_userprofile_vote_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='vote_count',
        ),
    ]