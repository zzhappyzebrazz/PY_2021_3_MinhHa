# Generated by Django 4.1.4 on 2022-12-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='image',
            field=models.ImageField(blank=True, default='store/images/avatar.jpg', null=True, upload_to='store/users/'),
        ),
    ]