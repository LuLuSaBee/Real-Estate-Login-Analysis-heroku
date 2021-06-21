from django.db import models


class RealEstate(models.Model):
    cotID = models.CharField(max_length=1, default='-')
    mdate = models.DateTimeField(default='1000-01-01T00:00:00Z')
    caseID = models.CharField(max_length=20, default='-')
    districtID = models.CharField(max_length=20, default='-')
    district = models.CharField(max_length=3, default='-')
    tranType = models.CharField(max_length=10, default='-')
    tran_tp_fg = models.CharField(max_length=1, default='-')
    tsign = models.CharField(max_length=30, default='-')
    tsign_fg = models.CharField(max_length=2, default='-')
    location = models.CharField(max_length=100, default='-')
    road_fg = models.CharField(max_length=1, default='-')
    coord_x = models.DecimalField(
        max_digits=21, decimal_places=8, default=0)
    coord_y = models.DecimalField(
        max_digits=21, decimal_places=8, default=0)
    land = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    build = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    berth = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    land_area = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)
    zoning = models.CharField(max_length=50, default='-')
    zoning_fg = models.CharField(max_length=2, default='-')
    ncity_z = models.CharField(max_length=50, default='-')
    ncity_z_fg = models.CharField(max_length=2, default='-')
    land_use = models.CharField(max_length=50, default='-')
    land_use_fg = models.CharField(max_length=2, default='-')
    tran_floor = models.CharField(max_length=100, default='-')
    tran_up_ll = models.DecimalField(
        max_digits=5, decimal_places=0, default=0)
    tran_single = models.CharField(max_length=1, default='-')
    tot_floor = models.DecimalField(
        max_digits=5, decimal_places=0, default=0)
    top_floor = models.CharField(max_length=10, default='-')
    bstate = models.CharField(max_length=50, default='-')
    bstate_fg = models.CharField(max_length=2, default='-')
    mainuse = models.CharField(max_length=50, default='-')
    mainuse_fg = models.CharField(max_length=2, default='-')
    matl = models.CharField(max_length=50, default='-')
    matl_fg = models.CharField(max_length=2, default='-')
    build_dd = models.DateTimeField(default='1000-01-01T00:00:00Z')
    room_age = models.DecimalField(
        max_digits=5, decimal_places=1, default=0)
    build_area = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    room = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    hall = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    health = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    compart = models.CharField(max_length=1, default='-')
    mgt_com = models.CharField(max_length=1, default='-')
    berth_tp = models.CharField(max_length=30, default='-')
    berth_tp_fg = models.CharField(max_length=1, default='-')
    berth_area = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    tot_prc = models.DecimalField(
        max_digits=10, decimal_places=1, default=0)
    unit_prc = models.DecimalField(
        max_digits=10, decimal_places=1, default=0)
    berth_prc = models.DecimalField(
        max_digits=10, decimal_places=1, default=0)
    rmk = models.CharField(max_length=200, default='-')
    ann_date = models.DateTimeField(default='1000-01-01T00:00:00Z')
    abnorm_td = models.CharField(max_length=1, default='-')
    abnorm_loc = models.CharField(max_length=1, default='-')
    abnorm_prc = models.CharField(max_length=1, default='-')

    def __str__(self):
        return self.caseID


class ColumnDescription(models.Model):
    name = models.CharField(max_length=50)
    columnName = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TotalValue(models.Model):
    date = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=100, decimal_places=1, default=0)
    total = models.DecimalField(
        max_digits=100, decimal_places=0, default=0)

    def __str__(self):
        return self.date
