# Generated by Django 4.2.4 on 2023-10-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, default='../static/imgs/profile-image-default.png', null=True, upload_to='profile_images/'),
        ),
    ]