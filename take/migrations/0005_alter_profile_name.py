

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=99, null=True),
        ),
    ]
