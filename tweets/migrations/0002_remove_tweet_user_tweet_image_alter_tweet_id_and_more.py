# Generated by Django 4.2 on 2023-04-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tweet",
            name="user",
        ),
        migrations.AddField(
            model_name="tweet",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="tweet",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="tweet",
            name="text",
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
    ]
