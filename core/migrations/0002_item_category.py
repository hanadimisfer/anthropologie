# Generated by Django 2.2 on 2020-09-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('F', 'Furniture'), ('D', 'Dining'), ('A', 'Accessories')], default='F', max_length=2),
            preserve_default=False,
        ),
    ]