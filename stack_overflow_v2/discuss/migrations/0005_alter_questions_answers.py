# Generated by Django 3.2.8 on 2022-07-15 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0004_auto_20220715_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discuss.answers'),
        ),
    ]
