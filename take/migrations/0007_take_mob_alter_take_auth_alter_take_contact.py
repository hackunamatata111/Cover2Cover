

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take', '0006_take_cname_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='take',
            name='mob',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='take',
            name='auth',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='take',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
