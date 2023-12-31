# Generated by Django 4.2.8 on 2023-12-15 13:34

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
            name='Item',
            fields=[
                ('item_id', models.TextField(primary_key=True, serialize=False)),
                ('item_description', models.TextField()),
                ('item_state', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_loan', models.DateField()),
                ('loan_due_date', models.DateField()),
                ('loan_is_finished', models.BooleanField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request_handler.item')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
