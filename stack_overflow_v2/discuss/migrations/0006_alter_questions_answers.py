# Generated by Django 3.2.8 on 2022-07-15 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0005_alter_questions_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answers',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='discuss.answers'),
            preserve_default=False,
        ),
    ]
