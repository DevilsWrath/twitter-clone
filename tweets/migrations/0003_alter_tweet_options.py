# Generated by Django 4.2 on 2023-04-14 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0002_remove_tweet_user_tweet_image_alter_tweet_id_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tweet",
            options={"ordering": ["-id"]},
        ),
    ]
