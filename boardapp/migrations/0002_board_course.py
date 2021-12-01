# Generated by Django 3.2.9 on 2021-11-30 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='board', to='courseapp.course'),
        ),
    ]