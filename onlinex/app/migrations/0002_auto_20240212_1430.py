# Generated by Django 3.2.12 on 2024-02-12 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
