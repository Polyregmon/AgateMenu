# Generated by Django 4.2.1 on 2023-07-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_itemmenu_des_eng'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]