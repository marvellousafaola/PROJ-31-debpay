# Generated by Django 4.0.5 on 2022-08-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Debtor', '0003_debtor_school_alter_debtor_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='debtor',
            name='debtor_image',
            field=models.ImageField(null=True, upload_to='debtors pics'),
        ),
    ]