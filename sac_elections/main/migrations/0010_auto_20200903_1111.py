# Generated by Django 3.1.1 on 2020-09-03 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200903_1109'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('voter', 'category')},
        ),
    ]