# Generated by Django 3.2.3 on 2021-06-21 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('columnName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotID', models.CharField(max_length=1)),
                ('mdate', models.DateTimeField()),
                ('caseID', models.CharField(max_length=20)),
                ('districtID', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=3)),
                ('tranType', models.CharField(max_length=10)),
                ('tran_tp_fg', models.CharField(max_length=1)),
                ('tsign', models.CharField(max_length=30)),
                ('tsign_fg', models.CharField(max_length=2)),
                ('location', models.CharField(max_length=100)),
                ('road_fg', models.CharField(max_length=1)),
                ('coord_x', models.DecimalField(decimal_places=8, max_digits=21)),
                ('coord_y', models.DecimalField(decimal_places=8, max_digits=21)),
                ('land', models.DecimalField(decimal_places=0, max_digits=9)),
                ('build', models.DecimalField(decimal_places=0, max_digits=9)),
                ('berth', models.DecimalField(decimal_places=0, max_digits=9)),
                ('land_area', models.DecimalField(decimal_places=2, max_digits=15)),
                ('zoning', models.CharField(max_length=50)),
                ('zoning_fg', models.CharField(max_length=2)),
                ('ncity_z', models.CharField(max_length=50)),
                ('ncity_z_fg', models.CharField(max_length=2)),
                ('land_use', models.CharField(max_length=50)),
                ('land_use_fg', models.CharField(max_length=2)),
                ('tran_floor', models.CharField(max_length=100)),
                ('tran_up_ll', models.DecimalField(decimal_places=0, max_digits=5)),
                ('tran_single', models.CharField(max_length=1)),
                ('tot_floor', models.DecimalField(decimal_places=0, max_digits=5)),
                ('top_floor', models.CharField(max_length=10)),
                ('bstate', models.CharField(max_length=50)),
                ('bstate_fg', models.CharField(max_length=2)),
                ('mainuse', models.CharField(max_length=50)),
                ('mainuse_fg', models.CharField(max_length=2)),
                ('matl', models.CharField(max_length=50)),
                ('matl_fg', models.CharField(max_length=2)),
                ('build_dd', models.DateTimeField()),
                ('room_age', models.DecimalField(decimal_places=1, max_digits=5)),
                ('build_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('room', models.DecimalField(decimal_places=0, max_digits=9)),
                ('hall', models.DecimalField(decimal_places=0, max_digits=9)),
                ('health', models.DecimalField(decimal_places=0, max_digits=9)),
                ('compart', models.CharField(max_length=1)),
                ('mgt_com', models.CharField(max_length=1)),
                ('berth_tp', models.CharField(max_length=30)),
                ('berth_tp_fg', models.CharField(max_length=1)),
                ('berth_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tot_prc', models.DecimalField(decimal_places=1, max_digits=10)),
                ('unit_prc', models.DecimalField(decimal_places=1, max_digits=10)),
                ('berth_prc', models.DecimalField(decimal_places=1, max_digits=10)),
                ('rmk', models.CharField(max_length=200)),
                ('ann_date', models.DateTimeField()),
                ('abnorm_td', models.CharField(max_length=1)),
                ('abnorm_loc', models.CharField(max_length=1)),
                ('abnorm_prc', models.CharField(max_length=1)),
            ],
        ),
    ]
