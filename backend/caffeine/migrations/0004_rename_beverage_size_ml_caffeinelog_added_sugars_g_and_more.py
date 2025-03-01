# Generated by Django 5.1.6 on 2025-02-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caffeine', '0003_rename_caffeine_caffeinelog_caffeine_mg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caffeinelog',
            old_name='beverage_size_ml',
            new_name='added_sugars_g',
        ),
        migrations.RenameField(
            model_name='caffeinelog',
            old_name='sugar_content_g',
            new_name='protein_g',
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='b_vitamins',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='other_ingredients',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='serving_size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='sodium_mg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='sugars_g',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='taurine_mg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='total_carbohydrates_g',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caffeinelog',
            name='total_fat_g',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
