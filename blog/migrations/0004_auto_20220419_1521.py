# Generated by Django 2.2.5 on 2022-04-19 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220418_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-modify_dt',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]
