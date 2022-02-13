

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take', '0005_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='take',
            name='cname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
