

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take', '0002_take_roll'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='take',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='take',
            name='course',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
