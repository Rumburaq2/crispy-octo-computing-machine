# Generated by Django 4.2.8 on 2023-12-17 13:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request_handler', '0002_alter_loan_date_of_loan'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loan',
            new_name='loans',
        ),
    ]