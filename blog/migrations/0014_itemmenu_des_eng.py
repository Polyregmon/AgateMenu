# Generated by Django 4.2.1 on 2023-05-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_itemmenu_eng_alter_itemmenu_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmenu',
            name='des_eng',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
