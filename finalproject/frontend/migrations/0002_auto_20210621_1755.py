# Generated by Django 3.2.3 on 2021-06-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=1, default=0, max_digits=100)),
                ('total', models.DecimalField(decimal_places=0, default=0, max_digits=100)),
            ],
        ),
        migrations.AlterField(
            model_name='realestate',
            name='abnorm_loc',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='abnorm_prc',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='abnorm_td',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='ann_date',
            field=models.DateTimeField(default='1000-01-01T00:00:00Z'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='berth',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='berth_area',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='berth_prc',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='berth_tp',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='berth_tp_fg',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='bstate',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='bstate_fg',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='build',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='build_area',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='build_dd',
            field=models.DateTimeField(default='1000-01-01T00:00:00Z'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='caseID',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='compart',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='coord_x',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=21),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='coord_y',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=21),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='cotID',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='district',
            field=models.CharField(default='-', max_length=3),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='districtID',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='hall',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='health',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='land',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='land_area',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='land_use',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='land_use_fg',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='location',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='mainuse',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='mainuse_fg',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='matl',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='matl_fg',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='mdate',
            field=models.DateTimeField(default='1000-01-01T00:00:00Z'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='mgt_com',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='ncity_z',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='ncity_z_fg',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='rmk',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='road_fg',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='room',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='room_age',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='top_floor',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tot_floor',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tot_prc',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tranType',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tran_floor',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tran_single',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tran_tp_fg',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tran_up_ll',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tsign',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='tsign_fg',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='unit_prc',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='zoning',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='zoning_fg',
            field=models.CharField(default='-', max_length=2),
        ),
    ]
