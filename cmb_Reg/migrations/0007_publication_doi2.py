# Generated by Django 5.0.2 on 2024-03-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmb_Reg', '0006_remove_publication_publicationdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='doi2',
            field=models.CharField(default='', max_length=200),
        ),
    ]
