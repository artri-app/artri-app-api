from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "authentication",
            "0003_dailyfatiguereport_dailysleepreport_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="dailysleepreport",
            name="sleep_level",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="dailysleepreport",
            name="sleep_duration",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dailysleepreport",
            name="sleep_quality",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="dailyfatiguereport",
            name="fatigue_description",
            field=models.TextField(blank=True, default=""),
        ),
    ]
