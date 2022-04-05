# Generated by Django 3.2 on 2022-04-05 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0010_remove_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contact_from', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
