# Generated by Django 4.0.3 on 2022-03-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_alter_schedule_options_alter_recipe_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='yields',
            field=models.PositiveIntegerField(default=1, verbose_name='Porciones'),
        ),
    ]
