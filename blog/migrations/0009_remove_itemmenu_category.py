# Generated by Django 4.2.1 on 2023-05-26 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_itemmenu_category_itemmenu_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmenu',
            name='category',
        ),
    ]
