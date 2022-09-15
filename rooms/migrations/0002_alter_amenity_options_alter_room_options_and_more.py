# Generated by Django 4.1.1 on 2022-09-15 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name": "어메니티", "verbose_name_plural": "어메니티들"},
        ),
        migrations.AlterModelOptions(
            name="room",
            options={"verbose_name": "방", "verbose_name_plural": "방들"},
        ),
        migrations.AlterField(
            model_name="amenity",
            name="description",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(related_name="rooms", to="rooms.amenity"),
        ),
    ]