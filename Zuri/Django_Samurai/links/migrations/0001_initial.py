# Generated by Django 3.0.1 on 2022-06-28 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_url', models.URLField()),
                ('description', models.CharField(blank=True, max_length=200)),
                ('identifier', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]