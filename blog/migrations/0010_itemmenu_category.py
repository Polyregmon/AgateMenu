# Generated by Django 4.2.1 on 2023-05-26 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_itemmenu_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmenu',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemcat', to='blog.category'),
        ),
    ]
